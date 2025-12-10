from typing import Optional
from pydantic import BaseModel

class PersonaModel(BaseModel):

    id: Optional[str] = None
    dni: str
    nombre: str
    apellidos: str
    telefono: str
    correo: str