from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
import os

app = FastAPI(title="API de Mascotas")

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

client = MongoClient(MONGO_URL)
db = client["mascotas_db"]
collection = db["mascotas"]


class Mascota(BaseModel):
    nombre: str
    especie: str
    edad: int


@app.post("/mascotas")
def agregar_mascota(mascota: Mascota):
    resultado = collection.insert_one(mascota.model_dump())

    return {
        "id": str(resultado.inserted_id)
    }


@app.get("/mascotas")
def listar_mascotas():
    mascotas = []

    for mascota in collection.find():
        mascotas.append({
            "id": str(mascota["_id"]),
            "nombre": mascota["nombre"],
            "especie": mascota["especie"],
            "edad": mascota["edad"]
        })

    return mascotas