from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models import pet as schemas
from app.api.pets import api

router = APIRouter(prefix="/pets", tags=["pets"])

@router.get("/", response_model=list[schemas.Pet])
def list_pets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return api.get_pets(db, skip=skip, limit=limit)

@router.get("/{pet_id}", response_model=schemas.Pet)
def get_pet(pet_id: int, db: Session = Depends(get_db)):
    db_pet = api.get_pet(db, pet_id)
    if not db_pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    return db_pet

@router.post("/", response_model=schemas.Pet)
def create_pet(pet: schemas.PetCreate, db: Session = Depends(get_db)):
    return api.create_pet(db, pet)

@router.put("/{pet_id}", response_model=schemas.Pet)
def update_pet(pet_id: int, pet: schemas.PetUpdate, db: Session = Depends(get_db)):
    updated_pet = api.update_pet(db, pet_id, pet)
    if not updated_pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    return updated_pet

@router.delete("/{pet_id}")
def delete_pet(pet_id: int, db: Session = Depends(get_db)):
    deleted = api.delete_pet(db, pet_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Pet not found")
    return {"message": "Pet deleted successfully"}
