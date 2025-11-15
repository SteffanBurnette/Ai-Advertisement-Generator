from pymongo import MongoClient
import gridfs
import os 
from dotenv import load_dotenv

# Load env
load_dotenv(r"C:\Users\Steffan\Desktop\Ai_advertisement_generator\Ai-Advertisement-Generator\Ai_video_generator\.env")
URI = os.getenv("MONGO_CONNECTION_STRING")

print("Loaded URI:", URI)  # DEBUG

# Connect to DB
client = MongoClient(URI)
db = client["test"]

# Create GridFS bucket
custom_bucket = gridfs.GridFSBucket(db, bucket_name="myTestBucket")

# Path to your video
video_path = r"C:\Users\Steffan\Desktop\Ai_advertisement_generator\Ai-Advertisement-Generator\dialogue_example.mp4"

# Make sure file exists
print("File exists:", os.path.exists(video_path))  # DEBUG

# Upload file
with open(video_path, "rb") as f:
    with custom_bucket.open_upload_stream(
        "my_video.mp4",
        metadata={"contentType": "video/mp4"}
    ) as grid_in:
        grid_in.write(f.read())

print("Upload complete.")
