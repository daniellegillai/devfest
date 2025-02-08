from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps

app = Flask(__name__)
CORS(app)

# Connect to MongoDB (adjust the URI as needed)
client = MongoClient("mongodb+srv://ibrigido:devFest2025@cluster0.c6gcg.mongodb.net/health_tracker?retryWrites=true&w=majority")
db = client["health_tracker"]  # You can name your DB as you like
collection = db["body_parts"]  # This collection will hold your body parts and their data

@app.route("/body_parts/", methods=["POST"])
def create_body_part():
    try:
        body_part = request.json
        result = collection.insert_one(body_part)
        return jsonify({"message": "Body part created successfully", "id": str(result.inserted_id)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/body_parts/", methods=["GET"])
def get_body_parts():
    try:
        body_parts = list(collection.find())
        return dumps(body_parts), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/body_parts/<body_part_id>", methods=["GET"])
def get_body_part(body_part_id):
    try:
        body_part = collection.find_one({"_id": ObjectId(body_part_id)})
        if body_part:
            return dumps(body_part), 200
        else:
            return jsonify({"error": "Body part not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/body_parts/<body_part_id>", methods=["DELETE"])
def delete_body_part(body_part_id):
    try:
        result = collection.delete_one({"_id": ObjectId(body_part_id)})
        if result.deleted_count > 0:
            return jsonify({"message": "Body part deleted successfully"}), 200
        else:
            return jsonify({"error": "Body part not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=7777)
