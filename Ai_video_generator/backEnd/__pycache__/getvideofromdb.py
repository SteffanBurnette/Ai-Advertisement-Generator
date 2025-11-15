from pymongo import MongoClient
import gridfs
import os 
from dotenv import load_dotenv
from bson import ObjectId


# Load env
load_dotenv(r"C:\Users\Steffan\Desktop\Ai_advertisement_generator\Ai-Advertisement-Generator\Ai_video_generator\.env")
URI = os.getenv("MONGO_CONNECTION_STRING")

print("Loaded URI:", URI)  # DEBUG

# Connect to DB
client = MongoClient(URI)
db = client["test"]

# Create GridFS bucket
custom_bucket = gridfs.GridFSBucket(db, bucket_name="myTestBucket")

file =  custom_bucket.open_download_stream(ObjectId("691853306a9678b69262149e"))
contents =  file.read()

#file = custom_bucket.open_download_stream_by_name("my_video.mp4")
#contents = file.read()

#print(contents)
# Save video to a local file
output_path = "retrieved_video2.mp4"

with open(output_path, "wb") as f:
    f.write(contents)

print(f"Video saved to {output_path}")
