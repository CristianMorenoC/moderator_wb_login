import os
from fastapi import FastAPI
from app.api import auth
from tortoise.contrib.fastapi import register_tortoise
from dotenv import load_dotenv
# from secret import PASSWORD, USERNAME, DB, PORT

load_dotenv(dotenv_path="secret.env")
# Inicializa la aplicación FastAPI
app = FastAPI()

PORT = int(os.getenv("PORT"))
DB_USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("PASSWORD")
DB = os.getenv("DB")

register_tortoise(
    app,
    db_url=f"postgres://{DB_USERNAME}:{PASSWORD}@localhost:{PORT}/{DB}",
    modules={'models': ['app.config.schemas.user']},
    generate_schemas=True,
    add_exception_handlers=True,
)

print(f"Connecting to database at: postgres://{DB_USERNAME}:*****@localhost:{PORT}/{DB}")

# Incluye las rutas de autenticación
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
