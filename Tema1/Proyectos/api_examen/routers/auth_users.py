import jwt
from pydantic import BaseModel
from jwt.exceptions import InvalidTokenError, PyJWTError
from pwdlib import PasswordHash
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import *
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from db.client import db_client

router = APIRouter(prefix="/auth", tags=["auth"])

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

    
@router.post("/registro", response_model=User, status_code=201)
async def add_colegio(user: User):

    user.password = password_hash.hash(user.password)

    user_dict = user.model_dump()

    db_client.test.colegios.insert_one(user_dict)

    return HTTPException(status_code=201, detail="User registrado correctamente")



@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):

    user_db = user_schema(
            db_client.test.users.find_one({"username": form.username})
        )
    if user_db:
    # Si el usuario existe en la base de datos
    # Comprobamos las contraseñas

        user = User(**user_db)

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
async def get_current_user(token:str = Depends(oauth2)):

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
    
    user = User(**db_client.test.users.find_one({"username": username}))

    if user.disabled:
        # Si el usuario está deshabilitado lanzamos excepción
        raise HTTPException(status_code=400, detail="Usuario inactivo")

    # Retornamos un usuario correcto y habilitado
    return user

@router.get("/auth/me")
async def me(user: User = Depends(get_current_user)):
    return user