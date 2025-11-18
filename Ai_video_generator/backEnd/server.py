from flask import Flask, jsonify, Blueprint
from flask_cors import CORS
from pymongo import MongoClient
import gridfs
import sys
sys.path.insert(0, "../Ai_video_generator/backEnd/videoGenblueprint.py") 
from videoGenblueprint import videoGen_bp
from fetchVideoBP import fetchVideo
from auth_routes import auth_bp 

app = Flask(__name__)
CORS(app, support_credentials = True, origins = ["http://localhost3000"])

#Need to change later:
app.secret_key = b'Secret'

#Blueprint endpoints
app.register_blueprint(videoGen_bp, url_prefix = "/videoGen")
app.register_blueprint(fetchVideo, url_prefix = "/getVideo")
app.register_blueprint(auth_bp)


@app.route("/")
def basics():
    return jsonify({"message": "Flask is working!"})

#Basicx flask endpoint structure
@app.route("/api/data")
def get_data():
    data = {"key": "value"}
    return jsonify(data)


# Server is running
if __name__ == "__main__":
    app.run(debug = True)


