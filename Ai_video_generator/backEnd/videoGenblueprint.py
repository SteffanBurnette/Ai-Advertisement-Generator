from flask import Blueprint, request, jsonify, g, session
import time
from google import genai
from google.genai import types
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId
import gridfs
import os
from dotenv import load_dotenv

# Name of the blueprint
videoGen_bp = Blueprint("video_generation", __name__, url_prefix="/video")

# Load env vars
load_dotenv(
    "C:/Users/Steffan/Desktop/Ai_advertisement_generator/"
    "Ai-Advertisement-Generator/Ai_video_generator/.env"
)

API_KEY = os.getenv("GEMINI_API_KEY")
MONGO_URI = os.getenv("MONGO_CONNECTION_STRING")

# Google GenAI client
genai_client = genai.Client(api_key=API_KEY)

# Mongo client + DB + GridFS bucket
mongo_client = MongoClient(MONGO_URI, server_api=ServerApi("1"))
db = mongo_client["test"]
custom_bucket = gridfs.GridFSBucket(db, bucket_name="myTestBucket")
print("Loaded URI:", MONGO_URI)  # DEBUG


# --- User loading (from session) ---

@videoGen_bp.before_request
def load_current_user():
    """
    Loading the logged-in user id from the session into g.current_user_id.
    """
    user_id = session.get("user_id")
    g.current_user_id = ObjectId(user_id) if user_id else None


# --- Routes ---

@videoGen_bp.route("/generate_video", methods=["POST"])
def generate_video():
    """
    Expected JSON body format:
    {
        "prompt": "text describing advert",
        "name": "my_video_name_without_extension"
    }
    """
    #Verifying login status before generating video
    if g.current_user_id is None:
        return jsonify({"error": "You must be logged in to generate a video."}), 401

    #Getting the json data
    data = request.get_json() or {}
    prompt = data.get("prompt")
    name = data.get("name")

    #Ensuring that both fields are filled
    if not prompt or not name:
        return jsonify({"error": "Both 'prompt' and 'name' are required."}), 400

    # 1. Generate the video
    operation = genai_client.models.generate_videos(
        model="veo-3.1-generate-preview",
        prompt=prompt,
    )

    # 2. Poll until done
    while not operation.done:
        print("Waiting for video generation to complete...")
        time.sleep(10)
        operation = genai_client.operations.get(operation)

    # 3. Get generated video
    generated_video = operation.response.generated_videos[0]

    # 4. Downloading video bytes 
    video_bytes = genai_client.files.download(file=generated_video.video)

    # 5. Saving to disk 
    filename = f'{name}.mp4'      
    with open(filename, "wb") as f:
        f.write(video_bytes)
    print(f"Generated video saved to {filename}")

    # 6. Upload to Mongo / GridFS with userId in metadata
    #    So we can later query videos by user
    print("File exists:", os.path.exists(filename))  # DEBUG

    with open(filename, "rb") as f:
        with custom_bucket.open_upload_stream(
            filename,
            metadata={
                "contentType": "video/mp4",
                "userId": str(g.current_user_id),  # 🔑 link file to logged-in user
                "prompt": prompt,
            },
        ) as grid_in:
            grid_in.write(f.read())

    print("Upload complete.")

    return jsonify({"message": f"The video {filename} was successfully created"}), 200


@videoGen_bp.route("/my_videos", methods=["GET"])
def get_my_videos():
    """
    Return all videos created by the currently logged-in user,
    based on GridFS metadata.userId.
    """
    if g.current_user_id is None:
        return jsonify({"error": "You must be logged in to view your videos."}), 401

    user_id_str = str(g.current_user_id)

    
    #Connecting to the bucket that contains all of the file metadata
    files_collection = db["myTestBucket.files"]

    cursor = files_collection.find({"metadata.userId": user_id_str})
    videos = []

    for doc in cursor:
        videos.append(
            {
                "id": str(doc["_id"]),
                "filename": doc.get("filename"),
                "length": doc.get("length"),  # bytes size
                "uploadDate": doc.get("uploadDate"),
                "contentType": doc.get("metadata", {}).get("contentType"),
                "prompt": doc.get("metadata", {}).get("prompt"),
            }
        )

    return jsonify({"videos": videos}), 200
