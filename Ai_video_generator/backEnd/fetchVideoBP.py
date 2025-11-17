from flask import Blueprint, Flask, request, jsonify
import time
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import gridfs
import os
from dotenv import load_dotenv
from bson import ObjectId

#Name of the blueprint
fetchVideo = Blueprint("getVideoGen", __name__)

#Getting the neccessary credentials 
load_dotenv("C:/Users/Steffan/Desktop/Ai_advertisement_generator/Ai-Advertisement-Generator/Ai_video_generator/.env")

#Conencting to the mongoClient
URI = os.getenv("MONGO_CONNECTION_STRING")
mongo_client = MongoClient(URI, server_api = ServerApi('1'))
db = mongo_client["test"]
# Create GridFS bucket
custom_bucket = gridfs.GridFSBucket(db, bucket_name="myTestBucket")
print("Loaded URI:", URI)  # DEBUG

#The endpoints

#Takes a prompt and video file name to generate a video and save it with said name
@fetchVideo.route("/fetch_video", methods = {"GET"})
def get_videos():
    data = request.get_json()
    

    #file =  custom_bucket.open_download_stream(ObjectId("691853306a9678b69262149e"))
    #contents =  file.read()

    file = custom_bucket.open_download_stream_by_name(f"{data.get("name")}.mp4")
    contents = file.read()

    #print(contents)
    # Save video to a local file
    output_path = f"retrieved_{data.get("name")}.mp4"

    with open(output_path, "wb") as f:
        f.write(contents)

    print(f"Video saved to {output_path}")

    
    return jsonify({"Message": f"The video {data.get("name")}.mp4 was successfully downloaded"}), 200



