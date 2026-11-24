from pydantic import BaseModel

class PetBase(BaseModel):
    name: str
    species: str
    age: int

class PetCreate(PetBase):
    pass

class PetUpdate(PetBase):
    pass

class Pet(PetBase):
    id: int

    class Config:
        from_attributes = True
