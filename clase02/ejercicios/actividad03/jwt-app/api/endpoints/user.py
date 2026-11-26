from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from models.user import UserCreate, UserLogin
from database.mongo import user_collection
from api.auth import hash_password, verify_password, create_access_token, decode_token
from bson import ObjectId

router = APIRouter()
security = HTTPBearer()

def serialize_user(user):
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"]
    }



@router.post("/register")
def register(user: UserCreate):
    if user_collection.find_one({"username": user.username}):
        raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed = hash_password(user.password)
    new_user = {
        "username": user.username,
        "email": user.email,
        "password": hashed
    }
    result = user_collection.insert_one(new_user)
    return {"id": str(result.inserted_id)}

@router.get("/")
def list_users():
    return [serialize_user(user) for user in user_collection.find()]

@router.get("/{user_id}")
def get_user(user_id: str):
    user = user_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return serialize_user(user)

@router.put("/{user_id}")
def update_user(user_id: str, user: UserCreate):
    updated = user_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {
            "username": user.username,
            "email": user.email,
            "password": hash_password(user.password)
        }}
    )
    if updated.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated"}

@router.delete("/{user_id}")
def delete_user(user_id: str):
    deleted = user_collection.delete_one({"_id": ObjectId(user_id)})
    if deleted.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}