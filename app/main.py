from fastapi import FastAPI
from app.api import auth

# Inicializa la aplicación FastAPI
app = FastAPI()

# Incluye las rutas de autenticación
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
