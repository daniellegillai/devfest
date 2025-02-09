from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps
import json

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient("mongodb+srv://ibrigido:devFest2025@cluster0.c6gcg.mongodb.net/health_tracker?retryWrites=true&w=majority")
db = client["health_tracker"]  
collection = db["body_parts"]

@app.route("/body_parts/", methods=["POST"])
def create_body_part():
    try:
        body_part = request.json
        result = collection.insert_one(body_part)
        return jsonify({"message": "Body part created successfully", "id": str(result.inserted_id)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/body_parts/", methods=["GET"])
def get_body_parts(): # retrieves all the body parts
    try:
        body_parts = list(collection.find())
        return dumps(body_parts), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/body_parts/<body_part_id>", methods=["GET"])
def get_body_part(body_part_id): # retrieves all the data in one body part
    try:
        body_part = collection.find_one({"_id": ObjectId(body_part_id)})
        if body_part:
            return dumps(body_part), 200
        else:
            return jsonify({"error": "Body part not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/body_parts/<body_part_id>", methods=["DELETE"])
def delete_body_part(body_part_id): # don't think we need this for web app implementation
    try:
        result = collection.delete_one({"_id": ObjectId(body_part_id)})
        if result.deleted_count > 0:
            return jsonify({"message": "Body part deleted successfully"}), 200
        else:
            return jsonify({"error": "Body part not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route("/body_parts/history/add/<body_part_id>", methods=["POST"])
def add_history_entry(body_part_id):
    history_entry=request.json
    try:
        result = collection.update_one(
            {"_id": ObjectId(body_part_id)},
            {"$push": {"history": history_entry}}
        )
        if result.modified_count > 0:
            return jsonify({"message": "History added successfully"}), 200
        else:
            return jsonify({"error": "Body part not found or no changes made"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/body_parts/history/update/<body_part_id>", methods=["PUT"])
def update_history_entry(body_part_id):
    update_info = request.json  
    try:
        result = collection.update_one(
            {"_id": ObjectId(body_part_id)},
            {"$set": {f"history.{update_info['index']}": update_info['new_data']}}
        )
        if result.modified_count > 0:
            return jsonify({"message": "History updated successfully"}), 200
        else:
            return jsonify({"error": "No changes made or body part not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/body_parts/history/remove/<body_part_id>", methods=["POST"])
def remove_history_entry(body_part_id):
    entry_info = request.json  # Assume this contains the criteria to identify the entry, e.g., {"date": "2025-02-08"}
    try:
        result = collection.update_one(
            {"_id": ObjectId(body_part_id)},
            {"$pull": {"history": entry_info}}
        )
        if result.modified_count > 0:
            return jsonify({"message": "History entry removed successfully"}), 200
        else:
            return jsonify({"error": "No history found with provided info or body part not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    



if __name__ == "__main__":
    app.run(port=7778)

