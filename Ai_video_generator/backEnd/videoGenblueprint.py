from flask import Blueprint, Flask, request, jsonify
import time
from google import genai
from google.genai import types
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import gridfs
import os
from dotenv import load_dotenv


#Name of the blueprint
videoGen_bp = Blueprint("video_generation", __name__)

#Getting the neccessary credentials to use the model
load_dotenv("C:/Users/Steffan/Desktop/Ai_advertisement_generator/Ai-Advertisement-Generator/Ai_video_generator/.env")
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key = API_KEY)

#Conencting to the mongoClient

URI = os.getenv("MONGO_CONNECTION_STRING")
mongo_client = MongoClient(URI, server_api = ServerApi('1'))
db = mongo_client["test"]
# Create GridFS bucket
custom_bucket = gridfs.GridFSBucket(db, bucket_name="myTestBucket")
print("Loaded URI:", URI)  # DEBUG

#The endpoints

#Takes a prompt and video file name to generate a video and save it with said name
@videoGen_bp.route("/generate_video", methods = {"POST"})
def generate_video():
    data = request.get_json()
    #Generates the video based on the users prompt
    operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt=data.get("prompt"),
    )

    # Poll the operation status until the video is ready.
    while not operation.done:
        print("Waiting for video generation to complete...")
        time.sleep(10)
        operation = client.operations.get(operation)

    # Download the generated video.
    generated_video = operation.response.generated_videos[0]
    client.files.download(file=generated_video.video)
    generated_video.video.save(f"{data.get("name")}.mp4")
    print(f"Generated video saved to {data.get("name")}.mp4")

    
    #Uploading to mongo DB
    # Path to your video
    video_path = f"{data.get("name")}.mp4"
    # Make sure file exists
    print("File exists:", os.path.exists(video_path))  # DEBUG

   # Upload file
    with open(video_path, "rb") as f:
        with custom_bucket.open_upload_stream(
        f'{data.get("name")}.mp4',
        metadata={"contentType": "video/mp4"}
         ) as grid_in:
            grid_in.write(f.read())

    print("Upload complete.")

    
    return jsonify({"Message": f"The video {data.get("name")}.mp4 was successfully created"}), 200



