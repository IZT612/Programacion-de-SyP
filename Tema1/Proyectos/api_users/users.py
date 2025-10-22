from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

#Entidad persona
class User(BaseModel):

    id: int
    name: str
    surname: str
    age: int

lista_usuarios = [
    User(id=1, name="Carlos", surname="Pérez", age=28),
    User(id=2, name="Ana", surname="Gómez", age=34),
    User(id=3, name="Luis", surname="Martínez", age=41),
    User(id=4, name="Laura", surname="Hernández", age=23),
    User(id=5, name="Javier", surname="López", age=35),
    User(id=6, name="Sofía", surname="García", age=30),
    User(id=7, name="David", surname="Rodríguez", age=38),
    User(id=8, name="María", surname="Fernández", age=29),
    User(id=9, name="Pedro", surname="Jiménez", age=32),
    User(id=10, name="Eva", surname="Ruiz", age=27),
    User(id=11, name="Marta", surname="Sánchez", age=36),
    User(id=12, name="Antonio", surname="Díaz", age=43),
    User(id=13, name="Isabel", surname="Álvarez", age=40),
    User(id=14, name="José", surname="Castro", age=25),
    User(id=15, name="Carmen", surname="Vázquez", age=33),
    User(id=16, name="Francisco", surname="Moreno", age=44),
    User(id=17, name="Paula", surname="Gil", age=26),
    User(id=18, name="Raúl", surname="Torres", age=39),
    User(id=19, name="Julia", surname="Ramos", age=31),
    User(id=20, name="Miguel", surname="Vega", age=45)
]




def next_id():

    return max(lista_usuarios, key=lambda user: user.id).id + 1

@app.get("/users")
def user():
    
    return lista_usuarios

@app.get("/users/id")
def user(id: int):

    users = [user for user in lista_usuarios if user["id"] == id]

    if (len(users) == 0):
        return {"error": "no se ha encontrado el usuario"}
    else:
        return users
    
@app.get("/users/name")
def user(name: str):

    users = [user for user in lista_usuarios if user["name"] == name]

    if (len(users) == 0):
        return {"error": "no se ha encontrado el usuario"}
    else:
        return users
    
@app.post("/users", status_code=201, response_model=User)
def add_user(user: User):

    user.id = next_id()
    lista_usuarios.append(user)
    return user

@app.put("/users/{id}")
def modify_user(id: int, user: User):

    for index, saved_user in enumerate(lista_usuarios):
        if saved_user.id == id:
            user.id = id
            lista_usuarios[index] = user
            return user
        
    raise HTTPException(status_code = 404, detail = "User not found")

@app.delete("/users/{id}")
def delete_user(id: int):

    for saved_user in lista_usuarios:
        if saved_user.id == id:
            lista_usuarios.remove(saved_user)
            return {}
        
    raise HTTPException(status_code=404, detail = "User not found")