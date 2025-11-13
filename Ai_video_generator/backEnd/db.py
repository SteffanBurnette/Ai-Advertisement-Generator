from pymongo import MongoClient
import pymongo
import os 
from dotenv import load_dotenv

load_dotenv("C:/Users/Steffan/Desktop/Ai_advertisement_generator/Ai-Advertisement-Generator/Ai_video_generator/.env")
URI = os.getenv("MONGO_CONNECTION_STRING")

try:
    # start example code here
    uri = URI
    client = MongoClient(uri, server_api=pymongo.server_api.ServerApi(
       version="1", strict=True, deprecation_errors=True))

    # end example code here

    client.admin.command("ping")
    print("Connected successfully")

    # other application code

    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)
