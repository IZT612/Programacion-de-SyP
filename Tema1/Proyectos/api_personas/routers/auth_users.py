import jwt
from pydantic import BaseModel
from jwt.exceptions import InvalidTokenError, PyJWTError
from pwdlib import PasswordHash
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import *

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# Algoritmo de encriptación
ALGORITHM = "HS256"

# Duración del token.
ACCESS_TOKEN_EXPIRE_MINUTES = 5

# Clave usada como semilla para generar el token
# openssl rand -hex 32
SECRET_KEY = "87ab51098990feb4a2f78da9c911187a71290ebd9e98e56d8b24090815f2ce6f"

# Objeto que se usará para el cálculo del hash y la verificación de las contraseñas
password_hash = PasswordHash.recommended()  

class User(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {

    "ivanzt" :{
        "username": "ivanzt",
        "fullname": "Iván Zamora Torres",
        "email": "ivan.zamora@iesnervion.es",
        "disabled": False,
        "password": PasswordHash.recommended().hash("1234")
    },

    "admin" :{
        "username": "admin",
        "fullname": "Admin",
        "email": "admin@gmail.com",
        "disabled": False,
        "password": PasswordHash.recommended().hash("adminpw")
    }

}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(users_db[username])

@router.post("/register", status_code=201)
def register(user: UserDB):
    if user.username not in users_db:
        hashed_password = password_hash.hash(user.password)
        user.password = hashed_password
        users_db[user.username] = user.model_dump()
        return user
    else:
        raise HTTPException(status_code = 409, detail="User already exists.")


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):

    user_db = users_db.get(form.username)
    if user_db:
    # Si el usuario existe en la base de datos
    # Comprobamos las contraseñas

        user = UserDB(**user_db)

        try:
            if password_hash.verify(form.password, user.password):
                expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
                access_token = {"sub": user.username, "exp":expire}
                # Generamos el token
                token = jwt.encode(access_token, SECRET_KEY, algorithm=ALGORITHM)
                return {"access_token":token, "token_type":"bearer"}
    #raise HTTPException(status_code=401, detail="Contraseña incorrecta")
        except:
            raise HTTPException(status_code=401, detail="Error en la autenticación.")
    raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos.")

# Esta función será nuestra dependencia
# Lo que pretendemos con esta función es que
# nos devuelva el usuario a partir del token
# En esta función, nuestra relación de dependencia es el objeto oauth2
async def authentication(token:str = Depends(oauth2)):

    # Para poder obtener el usuario a partir del token tenemos que desencriptarlo
    # con exactamente las mismas características que para encriptarlo
    # Como la llamada a get puede lanzar una excepción, la capturamos por si acaso
    try:
        username = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM).get("sub")
        # Nos aseguramos de que el usuario no es None
        if username is None:
            # Si es None lanzamos la excepción
            raise HTTPException(status_code=401, detail="Credenciales de autenticación inválidas", headers={"WWW-Authenticate" : "Bearer"})
        
    except PyJWTError:
        # Si ha fallado algo del proceso de la decodificación o si no ha encontrado la clave "sub"
        # lanzamos una excepción HTTP
        raise HTTPException(status_code=401,
        detail="Credenciales de autenticación inválidas", headers={"WWW-Authenticate" : "Bearer"})
    
    user = User(**users_db[username])

    if user.disabled:
        # Si el usuario está deshabilitado lanzamos excepción
        raise HTTPException(status_code=400, detail="Usuario inactivo")

    # Retornamos un usuario correcto y habilitado
    return user

@router.get("/auth/me")
async def me(user: User = Depends(authentication)):
    return user