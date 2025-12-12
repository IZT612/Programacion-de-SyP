from fastapi import APIRouter, HTTPException, Depends
from bson import ObjectId
from db.client import db_client
from db.schemas.alumno import alumno_schema, alumnos_schema
from db.schemas.colegio import colegio_schema, colegios_schema
from db.models.alumno import Alumno
from db.models.colegio import Colegio

router = APIRouter(prefix="/alumnos", tags=["alumnos"])

# Obtener todos los alumnos
@router.get("/", response_model=list[Alumno])
async def get_alumnos():
    return alumnos_schema(db_client.test.alumnos.find())


# Obtener alumno por curso y distrito del colegio (query ?id=123)
@router.get("", response_model=Alumno)
async def get_alumno(curso: str, distrito: str):

    if curso == "" and distrito == "":
        return alumnos_schema(db_client.test.alumnos.find())
    elif distrito == "":
        alumnos = get_alumnos_by_curso(curso)
    elif curso == "":
        alumnos = get_alumnos_by_distrito_colegio(distrito)
    else:
        alumnos = get_alumnos_by_curso(curso)
        alumnos += get_alumnos_by_distrito_colegio(distrito)

    return alumnos


# Obtener alumno por ID en la ruta
@router.get("/{id}", response_model=Alumno)
async def get_alumno(id: str):

    alumno = search_alumno_id(id)

    if not type(alumno) == Alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    else:
        return alumno
    
# Obtener alumno por ID de colegio en la ruta
@router.get("/colegio/{id}", response_model=Alumno)
async def get_alumno(id: str):

    if not colegio_existe(id):
        raise HTTPException(status_code=404, detail="Colegio no existente")

    alumnos = get_alumnos_by_id_colegio(id)

    return alumnos


# Crear nuevo alumno
@router.post("/", response_model=Alumno, status_code=201)
async def add_alumno(alumno: Alumno, authorized = Depends(auth_user)):

    # Comprobamos 
    if (not (colegio_existe(alumno.id_colegio) and tipo_curso_correcto(alumno.curso))):
        raise HTTPException(status_code=422, detail="")

    alumno_dict = alumno.model_dump()
    del alumno_dict["id"]  # el id lo genera Mongo

    id = db_client.test.alumnos.insert_one(alumno_dict).inserted_id
    alumno_dict["id"] = str(id)

    return HTTPException(status_code=201, detail="Alumno creado correctamente")

# Actualizar alumno
@router.put("/{id}", response_model = Alumno)
async def modify_alumno(id: str, new_alumno: Alumno, authorized = Depends(auth_user)):

    alumno_dict = new_alumno.model_dump()
    del alumno_dict["id"]

    try:
        db_client.test.alumnos.find_one_and_replace(
            {"_id": ObjectId(id)},
            alumno_dict
        )
        return HTTPException(status_code=200, detail="Alumno actualizado")
    except:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    
# Eliminar alumno
@router.delete("/{id}", response_model=Alumno)
async def delete_alumno(id: str, authorized = Depends(auth_user)):
    found = db_client.test.alumnos.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")

    return HTTPException(status_code=200, detail="Alumno eliminado correctamente")


# Funciones de busqueda y comprobaciones

def search_alumno_id(id: str):
    try:
        alumno = alumno_schema(
            db_client.test.alumnos.find_one({"_id": ObjectId(id)})
        )
        return Alumno(**alumno)
    except:
        return {"error": "Alumno no encontrado"}
    
def colegio_existe(id: str):

    existe: bool = False

    
    colegio = colegio_schema(
        db_client.test.colegios.find_one({"_id": ObjectId(id)})
    )
    if type(colegio) == Colegio:
        existe = True

    return existe

def tipo_curso_correcto(curso: str):

    correcto: bool = False

    if(curso == "1ESO" or curso == "2ESO" or curso == "3ESO" or curso == "4ESO" or curso == "1BACH" or curso == "2BACH"):
        correcto = True

    return correcto

def get_alumnos_by_curso(curso: str):

    try:

        alumnos = alumnos_schema(
            db_client.test.personas.find_one({"curso": curso})
        )

        listaAlumnos = Alumno([alumno for alumno in alumnos ])

        return listaAlumnos
    except:
        return {"error": "Alumnos no encontrados"}
    
def get_alumnos_by_distrito_colegio(distrito: str):

    try:

        colegios = colegios_schema(
            db_client.test.personas.find_one({"distrito": distrito})
        )

        listaColegios = Colegio([colegio for colegio in colegios])

        listaAlumnos = Alumno([get_alumnos_by_id_colegio(colegio.id) for colegio in listaColegios])

        return listaAlumnos
    except:
        return {"error": "Alumnos no encontrados"}
    
def get_alumnos_by_id_colegio(id_colegio: str):

    try:

        alumnos = alumnos_schema(
            db_client.test.personas.find_one({"id_colegio": id_colegio})
        )

        listaAlumnos = Alumno([alumno for alumno in alumnos ])

        return listaAlumnos
    except:
        return {"error": "Alumnos no encontrados"}

    
