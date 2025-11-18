from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId
import os
from dotenv import load_dotenv



auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# Load env vars
load_dotenv("C:/Users/Steffan/Desktop/Ai_advertisement_generator/Ai-Advertisement-Generator/Ai_video_generator/.env")
MONGO_URI = os.getenv("MONGO_CONNECTION_STRING")

# Mongo client + DB + collection
mongo_client = MongoClient(MONGO_URI, server_api=ServerApi("1"))
db = mongo_client["test"]
users_col = db["users"]


# Helper: convert Mongo user to JSON-safe dict
def user_to_json(user_doc):
    return {
        "id": str(user_doc["_id"]),
        "email": user_doc["email"],
        "name": user_doc.get("name")
    }


# Endpoints

@auth_bp.route("/signup", methods=["POST"])
def signup():
    """
    Expected Request JSON Body Format:
    {
        "email": "user@example.com",
        "password": "secret123",
        "name": "Steffan"
    }
    """
    data = request.get_json() or {}
    email = data.get("email")
    password = data.get("password")
    name = data.get("name")

    # Basic validation
    if not email or not password:
        return jsonify({"error": "Email and password are required."}), 400

    # Check if user already exists
    existing = users_col.find_one({"email": email})
    if existing:
        return jsonify({"error": "User with that email already exists."}), 409

    # Hash password
    hashed_pw = generate_password_hash(password)

    # Create user
    new_user = {
        "email": email,
        "password": hashed_pw,
        "name": name,
    }
    result = users_col.insert_one(new_user)
    new_user["_id"] = result.inserted_id

    # Log the user in (store in session)
    session["user_id"] = str(result.inserted_id)

    return jsonify({
        "message": "Signup successful.",
        "user": user_to_json(new_user)
    }), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    """
    Expected Request JSON Body Format:
    {
        "email": "user@example.com",
        "password": "secret123"
    }
    """
    data = request.get_json() or {}
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required."}), 400

    user = users_col.find_one({"email": email})
    if not user:
        return jsonify({"error": "Invalid email or password."}), 401

    # Check password
    if not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid email or password."}), 401

    # Store user id in session
    session["user_id"] = str(user["_id"])

    return jsonify({
        "message": "Login successful.",
        "user": user_to_json(user)
    }), 200


@auth_bp.route("/me", methods=["GET"])
def get_current_user():
    """
    Returns the currently logged-in user based on the session.
    """
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"user": None}), 200

    user = users_col.find_one({"_id": ObjectId(user_id)})
    if not user:
        return jsonify({"user": None}), 200

    return jsonify({"user": user_to_json(user)}), 200


@auth_bp.route("/logout", methods=["POST"])
def logout():
    """
    Logs out the current user (clears session).
    """
    session.pop("user_id", None)
    return jsonify({"message": "Logged out."}), 200
