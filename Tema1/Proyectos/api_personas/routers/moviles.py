from fastapi import FastAPI, HTTPException, APIRouter, Depends
from pydantic import BaseModel

router = APIRouter(prefix="/moviles", tags=["moviles"])

class Movil(BaseModel):
    id: int
    precio_coste: float
    precio_venta: float
    id_persona: int

lista_moviles = [
    Movil(id = 1, precio_coste = 100, precio_venta = 130, id_persona = 20),
    Movil(id = 2, precio_coste = 110, precio_venta = 140, id_persona = 19),
    Movil(id = 3, precio_coste = 105, precio_venta = 135, id_persona = 18),
    Movil(id = 4, precio_coste = 120, precio_venta = 150, id_persona = 17),
    Movil(id = 5, precio_coste = 115, precio_venta = 145, id_persona = 16),
    Movil(id = 6, precio_coste = 125, precio_venta = 155, id_persona = 15),
    Movil(id = 7, precio_coste = 130, precio_venta = 160, id_persona = 14),
    Movil(id = 8, precio_coste = 135, precio_venta = 165, id_persona = 13),
    Movil(id = 9, precio_coste = 140, precio_venta = 170, id_persona = 12),
    Movil(id = 10, precio_coste = 145, precio_venta = 175, id_persona = 11),
    Movil(id = 11, precio_coste = 150, precio_venta = 180, id_persona = 10),
    Movil(id = 12, precio_coste = 155, precio_venta = 185, id_persona = 9),
    Movil(id = 13, precio_coste = 160, precio_venta = 190, id_persona = 8),
    Movil(id = 14, precio_coste = 165, precio_venta = 195, id_persona = 7),
    Movil(id = 15, precio_coste = 170, precio_venta = 200, id_persona = 6),
    Movil(id = 16, precio_coste = 175, precio_venta = 205, id_persona = 5),
    Movil(id = 17, precio_coste = 180, precio_venta = 210, id_persona = 4),
    Movil(id = 18, precio_coste = 185, precio_venta = 215, id_persona = 3),
    Movil(id = 19, precio_coste = 190, precio_venta = 220, id_persona = 2),
    Movil(id = 20, precio_coste = 195, precio_venta = 225, id_persona = 1)
]

def next_id():
   
   return max(lista_moviles, key=lambda movil_lambda: movil_lambda.id).id + 1

@router.get("/")
def movil():
    return lista_moviles

@router.get("/{id}")
def movil(id: int):

    moviles = [movil for movil in lista_moviles if movil.id == id]
    
    if len(moviles) != 0:
        return moviles
    else:
        return {"error" : "Movil no encontrado"}
    
@router.get("/persona/{id_persona}")
def movil(id_persona: int):

    moviles = [movil for movil in lista_moviles if movil.id_persona == id_persona]

    if len(moviles) != 0:
        return moviles
    else:
        return {"error" : "Movil no encontrado"}

@router.post("/", status_code=201, response_model=Movil)
def movil(movil: Movil):

    movil.id = next_id()
    lista_moviles.append(movil)
    return movil

@router.put("/{id}")
def movil(id: int, movil: Movil):

    for index, movil_guardado in enumerate(lista_moviles):

        if movil_guardado.id == id:

            movil.id = id
            lista_moviles[index] = movil
            return movil
        
    raise HTTPException(status_code = 404, detail = "User not found")

@router.delete("/{id}")
def movil(id: int):

    for movil_guardado in lista_moviles:

        if movil_guardado.id == id:

            lista_moviles.remove(movil_guardado)
            return {}
        
    raise HTTPException(status_code = 404, detail = "User not found")