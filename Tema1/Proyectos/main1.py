from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Entidad persona
class Persona(BaseModel):

    id: int
    dni: str
    nombre: str
    apellidos: str
    telefono: str
    correo: str

# La lista con datos:
lista_personas = [
  {"id": 1, "dni": "11111111A", "nombre": "Paco", "apellidos": "Pérez Cano", "telefono": "111111111", "correo": "paquitoPerez@gmail.com"},
  {"id": 2, "dni": "22222222B", "nombre": "María", "apellidos": "Gómez Ruiz", "telefono": "222222222", "correo": "maria.gomezruiz@example.com"},
  {"id": 3, "dni": "33333333C", "nombre": "Luis", "apellidos": "Martínez López", "telefono": "333333333", "correo": "luis.martinez@example.com"},
  {"id": 4, "dni": "44444444D", "nombre": "Ana", "apellidos": "Santos Morales", "telefono": "444444444", "correo": "ana.santos@example.com"},
  {"id": 5, "dni": "55555555E", "nombre": "Carlos", "apellidos": "Domínguez Fernández", "telefono": "555555555", "correo": "carlos.dominguez@example.com"},
  {"id": 6, "dni": "66666666F", "nombre": "Lucía", "apellidos": "Vega Castillo", "telefono": "666666666", "correo": "lucia.vega@example.com"},
  {"id": 7, "dni": "77777777G", "nombre": "Javier", "apellidos": "Ortiz Navarro", "telefono": "777777777", "correo": "javier.ortiz@example.com"},
  {"id": 8, "dni": "88888888H", "nombre": "Sofía", "apellidos": "Ramírez Blanco", "telefono": "888888888", "correo": "sofia.ramirez@example.com"},
  {"id": 9, "dni": "99999999I", "nombre": "Miguel", "apellidos": "Herrera Gil", "telefono": "999999999", "correo": "miguel.herrera@example.com"},
  {"id": 10, "dni": "10101010J", "nombre": "Elena", "apellidos": "Ruiz Sánchez", "telefono": "610101010", "correo": "elena.ruiz@example.com"},
  {"id": 11, "dni": "12121212K", "nombre": "Roberto", "apellidos": "Molina Rivas", "telefono": "621212121", "correo": "roberto.molina@example.com"},
  {"id": 12, "dni": "13131313L", "nombre": "Isabel", "apellidos": "Marín Paredes", "telefono": "631313131", "correo": "isabel.marin@example.com"},
  {"id": 13, "dni": "14141414M", "nombre": "Diego", "apellidos": "Polo Fuentes", "telefono": "641414141", "correo": "diego.polo@example.com"},
  {"id": 14, "dni": "15151515N", "nombre": "Nuria", "apellidos": "Cruz Delgado", "telefono": "651515151", "correo": "nuria.cruz@example.com"},
  {"id": 15, "dni": "16161616O", "nombre": "Alberto", "apellidos": "Serrano Bravo", "telefono": "661616161", "correo": "alberto.serrano@example.com"},
  {"id": 16, "dni": "17171717P", "nombre": "Carmen", "apellidos": "Gil Torres", "telefono": "671717171", "correo": "carmen.gil@example.com"},
  {"id": 17, "dni": "18181818Q", "nombre": "Óscar", "apellidos": "Villas Gómez", "telefono": "681818181", "correo": "oscar.villas@example.com"},
  {"id": 18, "dni": "19191919R", "nombre": "Patricia", "apellidos": "Montero León", "telefono": "691919191", "correo": "patricia.montero@example.com"},
  {"id": 19, "dni": "20202020S", "nombre": "Fernando", "apellidos": "Calvo Romero", "telefono": "702020202", "correo": "fernando.calvo@example.com"},
  {"id": 20, "dni": "21212121T", "nombre": "Marta", "apellidos": "Iglesias Peña", "telefono": "712121212", "correo": "marta.iglesias@example.com"}
]

@app.get("/personas/")
def persona():
    return lista_personas

@app.get("/personas/{id}")
def persona(id: int):
    personas = [persona for persona in lista_personas if persona["id"] == id]

    if len(personas) != 0:
        return personas[0]
    else:
      return {"error": "No person found."}
    
@app.get("/personas/dni/{dni}")
def persona(dni: str):
    personas = [persona for persona in lista_personas if persona["dni"] == dni]

    if len(personas) != 0:
        return personas[0]
    else:
      return {"error": "No person found."}
    
@app.get("/personas/nombre/{nombre}")
def persona(nombre: str):
    personas = [persona for persona in lista_personas if persona["nombre"] == nombre]

    if len(personas) != 0:
        return personas[0]
    else:
      return {"error": "No person found."}
    
@app.get("/personas/telefono/{telefono}")
def persona(telefono: str):
    personas = [persona for persona in lista_personas if persona["telefono"] == telefono]

    if len(personas) != 0:
        return personas[0]
    else:
      return {"error": "No person found."}
    
@app.get("/personas/correo/{correo}")
def persona(correo: str):
    personas = [persona for persona in lista_personas if persona["correo"] == correo]

    if len(personas) != 0:
        return personas[0]
    else:
      return {"error": "No person found."}