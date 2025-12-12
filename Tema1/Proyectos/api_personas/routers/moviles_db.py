from fastapi import APIRouter, HTTPException
from bson import ObjectId
from db.client import db_client
from db.models.MovilModel import Movil
from db.schemas.movil import movil_schema, moviles_schema

router = APIRouter(prefix="/movilesdb", tags=["movilesdb"])


# Obtener todos los móviles
@router.get("/", response_model=list[Movil])
async def get_moviles():
    return moviles_schema(db_client.test.moviles.find())


# Obtener móvil por ID (query ?id=123)
@router.get("", response_model=Movil)
async def get_movil(id: str):
    return search_movil_id(id)


# Obtener móvil por ID en la ruta
@router.get("/{id}", response_model=Movil)
async def get_movil(id: str):
    return search_movil_id(id)


# Crear un nuevo móvil
@router.post("/", response_model=Movil, status_code=201)
async def add_movil(movil: Movil):

    movil_dict = movil.model_dump()
    del movil_dict["id"]  # El ID lo genera MongoDB

    # Insertamos en la base de datos
    inserted_id = db_client.test.moviles.insert_one(movil_dict).inserted_id

    movil_dict["id"] = str(inserted_id)
    return Movil(**movil_dict)


# Modificar un móvil existente
@router.put("/{id}", response_model=Movil)
async def modify_movil(id: str, new_movil: Movil):

    movil_dict = new_movil.model_dump()
    del movil_dict["id"]

    try:
        db_client.test.moviles.find_one_and_replace(
            {"_id": ObjectId(id)}, movil_dict
        )
        return search_movil_id(id)
    except:
        raise HTTPException(status_code=404, detail="Movil no encontrado")


# Eliminar móvil por ID
@router.delete("/{id}", response_model=Movil)
async def delete_movil(id: str):

    found = db_client.test.moviles.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        raise HTTPException(status_code=404, detail="Movil no encontrado")

    return Movil(**movil_schema(found))


# ===========================
# Funciones auxiliares
# ===========================

def search_movil_id(id: str):
    try:
        movil = movil_schema(
            db_client.test.moviles.find_one({"_id": ObjectId(id)})
        )
        return Movil(**movil)
    except:
        return {"error": "Movil no encontrado"}
