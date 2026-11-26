from pydantic import BaseModel

class CharacterCreate(BaseModel):
    hitpoints: int
    num_lives: int
    damage_per_attack: int

