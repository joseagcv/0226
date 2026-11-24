from sqlalchemy.orm import Session
from app.db import models
from app.models import pet 

def get_pets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pet).offset(skip).limit(limit).all()

def get_pet(db: Session, pet_id: int):
    return db.query(models.Pet).filter(models.Pet.id == pet_id).first()

def create_pet(db: Session, pet: pet.PetCreate):
    db_pet = models.Pet(**pet.dict())
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet

def update_pet(db: Session, pet_id: int, pet: pet.PetUpdate):
    db_pet = get_pet(db, pet_id)
    if not db_pet:
        return None
    for key, value in pet.dict().items():
        setattr(db_pet, key, value)
    db.commit()
    db.refresh(db_pet)
    return db_pet

def delete_pet(db: Session, pet_id: int):
    db_pet = get_pet(db, pet_id)
    if db_pet:
        db.delete(db_pet)
        db.commit()
        return True
    return False
