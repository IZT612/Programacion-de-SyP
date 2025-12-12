from fastapi import FastAPI
from routers import alumnos, auth_users, colegios

app = FastAPI()

# Routers
app.include_router(alumnos.router)
app.include_router(auth_users.router)
app.include_router(colegios.router)