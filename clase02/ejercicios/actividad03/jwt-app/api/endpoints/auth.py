from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from models.user import UserCreate, UserLogin
from database.mongo import user_collection
from api.auth import hash_password, verify_password, create_access_token, decode_token
from bson import ObjectId

router = APIRouter()
security = HTTPBearer()

# Helper: convertir ObjectId a str
def serialize_user(user):
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"]
    }


@router.post("/login")
def login(credentials: UserLogin):
    user = user_collection.find_one({"username": credentials.username})
    if not user or not verify_password(credentials.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    print(user)
    token = create_access_token({"sub": str(user["_id"])})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me")
def get_me(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token_data = decode_token(credentials.credentials)
    if not token_data:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    try:
        user_id = ObjectId(token_data["sub"])
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid user ID in token")

    user = user_collection.find_one({"_id": user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return serialize_user(user)

