from fastapi import FastAPI
from routers import moviles, personas, auth_users, personas_db, moviles_db

app = FastAPI()

# Routers
app.include_router(moviles.router)
app.include_router(personas.router)
app.include_router(auth_users.router)
app.include_router(personas_db.router)
app.include_router(moviles_db.router)