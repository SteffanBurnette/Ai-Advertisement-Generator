import os
from dotenv import load_dotenv

load_dotenv("C:/Users/Steffan/Desktop/Ai_advertisement_generator/Ai-Advertisement-Generator/Ai_video_generator/.env")
key = "GEMINI_API_KEY"
value = os.getenv(key)
print(value)
#"cwd": "${fileDirname}"