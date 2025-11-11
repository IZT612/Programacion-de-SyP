import jwt

from jwt.exceptions import InvalidTokenError

from pwdlib import PasswordHash

from fastapi import APIRouter, HTTPException

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(prefix="/login", tags=["login"])

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
        "password": "ivanpw"
    },

    "admin" :{
        "username": "admin",
        "fullname": "Admin",
        "email": "admin@gmail.com",
        "disabled": False,
        "password": "adminpw"
    }

}

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):

    # Miramos si el usuario existe en la Base de Datos
    user_db = users_db.get(form.username)

    # Si no está en la base de datos se lanza una excepción
    if not user_db:
        raise HTTPException(status_code = 400, detail="Usuario no encontrado")
    
    # Si está, creamos un objeto de tipo UserDB a partir de su información
    user = UserDB( **users_db[form.username])

    # Comprobamos que las contraseñas coinciden con verify
    if not password_hash.verify(form.password, user.hashed_password):

    # Si no coinciden lanzamos excepción
        raise HTTPException(status_code=400, detail="La contraseña no es correcta")
    
    # Tomamos la hora actual + el tiempo de expiración del token que es un min
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    # Parámetros de nuestro token: el ufake_users_dbsuario, fecha de expiración
    access_token = {"sub" : user.username, "exp":expire}

    # Para generar el token le pasamos la información a cifrar que es el usuario en sí y la fecha de expiración
    # También le pasamos la semilla y el algoritmo utilizado para generar el token
    token = jwt.encode(access_token, SECRET_KEY, algorithm=ALGORITHM)

    # Si todo va bien, devolvemos el token generado
    return {"access_token" : token, "token_type": "bearer"}

# Esta función será nuestra dependencia
# Lo que pretendemos con esta función es que
# nos devuelva el usuario a partir del token
# En esta función, nuestra relación de dependencia es el objeto oauth2
async def auth_user(token:str = Depends(oauth2)):

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