from typing import Optional
from pydantic import BaseModel

#Entidad movil
class Movil(BaseModel):

    id: Optional[str] = None
    precio_coste: str
    precio_venta: str
    id_persona: str