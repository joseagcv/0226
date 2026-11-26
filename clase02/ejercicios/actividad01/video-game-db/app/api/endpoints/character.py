from fastapi import APIRouter, Depends, HTTPException
from typing import Dict
from schema.character import CharacterCreate
from models.character import Character
import uuid
import csv
import os
import pymongo

router = APIRouter()
mongo_uri = os.environ.get('MONGO_URI', "mongodb://localhost:27017/")

# MongoDB setup
client = pymongo.MongoClient(mongo_uri)
db = client["mydatabase"]
collection = db["characters"]
client.server_info()
@router.post("/create")
def create_character(character: CharacterCreate):
    char_id = str(uuid.uuid4())
    new_character = Character(
        id=char_id,
        hitpoints=character.hitpoints,
        num_lives=character.num_lives,
        damage_per_attack=character.damage_per_attack
    )

    collection.insert_one(new_character.to_dict())
    return {"id": char_id, "character": new_character.to_dict()}


@router.get("/")
def get_all_characters():
    characters = list(collection.find({}, {'_id': 0}))
    return characters


@router.get("/{char_id}")
def get_character(char_id: str):
    char_data = collection.find_one({"id": char_id}, {'_id': 0})
    if not char_data:
        raise HTTPException(status_code=404, detail="Character not found")
    return char_data


@router.put("/{char_id}/evolve")
def evolve_character(char_id: str):
    char_data = collection.find_one({"id": char_id})
    if not char_data:
        raise HTTPException(status_code=404, detail="Character not found")

    character = Character(**{k: v for k, v in char_data.items() if k != "_id"})
    character.evolve()

    collection.update_one({"id": char_id}, {"$set": character.to_dict()})
    return character.to_dict()


@router.delete("/{char_id}")
def delete_character(char_id: str):
    result = collection.delete_one({"id": char_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Character not found")
    return {"detail": "Character deleted"}