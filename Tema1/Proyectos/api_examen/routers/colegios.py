from fastapi import APIRouter, HTTPException, Depends
from bson import ObjectId
from db.client import db_client
from db.schemas.colegio import colegio_schema, colegios_schema
from db.models.colegio import Colegio

router = APIRouter(prefix="/colegios", tags=["colegios"])

# Obtener todos los colegios
@router.get("/", response_model=list[Colegio])
async def get_colegios():
    return colegios_schema(db_client.test.colegios.find())


# Obtener colegio por id (query ?id=123)
@router.get("", response_model=Colegio)
async def get_colegio(id: str):

    colegio = search_colegio_id(id)

    if not type(colegio) == Colegio:
        raise HTTPException(status_code=404, detail="Colegio no encontrado")
    else:
        return colegio


# Obtener colegio por ID en la ruta
@router.get("/{id}", response_model=Colegio)
async def get_colegio(id: str):

    colegio = search_colegio_id(id)

    if not type(colegio) == Colegio:
        raise HTTPException(status_code=404, detail="Colegio no encontrado")
    else:
        return colegio


# Crear nuevo colegio
@router.post("/", response_model=Colegio, status_code=201)
async def add_colegio(colegio: Colegio):

    # Comprobamos si el tipo es correcto
    if (not tipo_colegio_correcto(colegio.tipo)):
        raise HTTPException(status_code=422, detail="Tipo de colegio incorrecto o JSON en formato invalido. Tipo debe ser 'publico', 'concertado', o 'privado'")

    colegio_dict = colegio.model_dump()
    del colegio_dict["id"]  # el id lo genera Mongo

    id = db_client.test.colegios.insert_one(colegio_dict).inserted_id
    colegio_dict["id"] = str(id)

    return HTTPException(status_code=201, detail="Colegio creado correctamente")

# Funciones de busqueda y comprobaciones

def search_colegio_id(id: str):
    try:
        colegio = colegio_schema(
            db_client.test.colegios.find_one({"_id": ObjectId(id)})
        )
        return Colegio(**colegio)
    except:
        return {"error": "colegio no encontrado"}
    
def tipo_colegio_correcto(tipo: str):

    correcto: bool = False

    if (tipo == "publico" or tipo == "concertado" or tipo == "privado"):

        correcto = True
    
    return correcto
