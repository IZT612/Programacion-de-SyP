from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from db.client import db_client
from db.schemas.persona import persona_schema, personas_schema
from db.models.PersonaModel import Persona

router = APIRouter(prefix="/personasdb", tags=["personasdb"])


# Obtener todas las personas
@router.get("/", response_model=list[Persona])
async def get_personas():
    return personas_schema(db_client.test.personas.find())


# Obtener persona por id (query ?id=123)
@router.get("", response_model=Persona)
async def get_persona(id: str):
    return search_persona_id(id)


# Obtener persona por ID en la ruta
@router.get("/{id}", response_model=Persona)
async def get_persona(id: str):
    return search_persona_id(id)


# Crear nueva persona
@router.post("/", response_model=Persona, status_code=201)
async def add_persona(persona: Persona):

    # Comprobamos si ya existe una persona con el mismo dni
    if type(search_persona_by_dni(persona.dni)) == Persona:
        raise HTTPException(status_code=409, detail="Persona ya existe con ese DNI")

    persona_dict = persona.model_dump()
    del persona_dict["id"]  # el id lo genera Mongo

    id = db_client.test.personas.insert_one(persona_dict).inserted_id
    persona_dict["id"] = str(id)

    return Persona(**persona_dict)


# Modificar persona existente
@router.put("/{id}", response_model=Persona)
async def modify_persona(id: str, new_persona: Persona):

    persona_dict = new_persona.model_dump()
    del persona_dict["id"]

    try:
        db_client.test.personas.find_one_and_replace(
            {"_id": ObjectId(id)},
            persona_dict
        )
        return search_persona_id(id)
    except:
        raise HTTPException(status_code=404, detail="Persona no encontrada")


# Eliminar persona
@router.delete("/{id}", response_model=Persona)
async def delete_persona(id: str):
    found = db_client.test.personas.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        raise HTTPException(status_code=404, detail="Persona no encontrada")

    return Persona(**persona_schema(found))


# ===========================
# Funciones de búsqueda
# ===========================

def search_persona_id(id: str):
    try:
        persona = persona_schema(
            db_client.test.personas.find_one({"_id": ObjectId(id)})
        )
        return Persona(**persona)
    except:
        return {"error": "Persona no encontrada"}


def search_persona_by_dni(dni: str):
    try:
        persona = persona_schema(
            db_client.test.personas.find_one({"dni": dni})
        )
        return Persona(**persona)
    except:
        return {"error": "Persona no encontrada"}
