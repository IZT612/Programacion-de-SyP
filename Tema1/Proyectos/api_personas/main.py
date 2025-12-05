from fastapi import FastAPI
from routers import moviles, personas, auth_users
from Tema1.Proyectos.api_personas.routers.db.models import personasModel

app = FastAPI()

# Routers
app.include_router(moviles.router)
app.include_router(personas.router)
app.include_router(auth_users.router)
app.include_router(personasModel.router)