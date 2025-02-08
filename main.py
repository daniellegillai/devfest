
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from motor import motor_asyncio
from typing import List

# Initialize the FastAPI app
app = FastAPI()

# Initialize the MongoDB client
client = motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/")
db = client["healthcare_database"]
collection = db["healthcare_data"]

# Define the BodyPart model
class BodyPart(BaseModel):
    id: str
    name: str
    data: List[str]

# Define the HealthcareData model
class HealthcareData(BaseModel):
    id: str
    body_part_id: str
    data: str

# Define the endpoint to create a new body part
@app.post("/body_parts/")
async def create_body_part(body_part: BodyPart):
    result = await collection.insert_one({"id": body_part.id, "name": body_part.name, "data": body_part.data})
    return {"message": "Body part created successfully"}

# Define the endpoint to get all body parts
@app.get("/body_parts/")
async def get_body_parts():
    body_parts = await collection.find().to_list(1000)
    return body_parts

# Define the endpoint to get a specific body part
@app.get("/body_parts/{body_part_id}")
async def get_body_part(body_part_id: str):
    body_part = await collection.find_one({"id": body_part_id})
    if body_part is None:
        raise HTTPException(status_code=404, detail="Body part not found")
    return body_part

# Define the endpoint to update a body part
@app.put("/body_parts/{body_part_id}")
async def update_body_part(body_part_id: str, body_part: BodyPart):
    result = await collection.update_one({"id": body_part_id}, {"$set": {"name": body_part.name, "data": body_part.data}})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Body part not found")
    return {"message": "Body part updated successfully"}

# Define the endpoint to delete a body part
@app.delete("/body_parts/{body_part_id}")
async def delete_body_part(body_part_id: str):
    result = await collection.delete_one({"id": body_part_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Body part not found")
    return {"message": "Body part deleted successfully"}

# Define the endpoint to create new healthcare data for a body part
@app.post("/healthcare_data/")
async def create_healthcare_data(healthcare_data: HealthcareData):
    result = await collection.update_one({"id": healthcare_data.body_part_id}, {"$push": {"data": healthcare_data.data}})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Body part not found")
    return {"message": "Healthcare data created successfully"}

# Define the endpoint to get all healthcare data for a body part
@app.get("/healthcare_data/{body_part_id}")
async def get_healthcare_data(body_part_id: str):
    body_part = await collection.find_one({"id": body_part_id})
    if body_part is None:
        raise HTTPException(status_code=404, detail="Body part not found")
    return body_part["data"]

# Define the endpoint to update healthcare data for a body part
@app.put("/healthcare_data/{body_part_id}/{data_id}")
async def update_healthcare_data(body_part_id: str, data_id: int, healthcare_data: HealthcareData):
    result = await collection.update_one({"id": body_part_id}, {"$set": {f"data.{data_id}": healthcare_data.data}})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Body part not found")
    return {"message": "Healthcare data updated successfully"}

# Define the endpoint to delete healthcare data for a body part
@app.delete("/healthcare_data/{body_part_id}/{data_id}")
async def delete_healthcare_data(body_part_id: str, data_id: int):
    result = await collection.update_one({"id": body_part_id}, {"$pull": {"data": {"$slice": [data_id, 1]}}})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Body part not found")
    return {"message": "Healthcare data deleted successfully"}
