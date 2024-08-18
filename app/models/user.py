from pydantic import BaseModel, EmailStr

# Modelo de usuario simulado
fake_users_db = {
"cristian.moreno.tech@gmail.com": {
        "username": "cristianfmoreno",
        "full_name": "Cristian Fabian Moreno Contreras",
        "hashed_password": "$2b$12$KIXg6eQ9a.VJjaEG1iEiqOlq5hfTymu7Mya6hQ21VZB1SxV8pXcOq",  # hashed version of "password"
        "disabled": False,
    },
    "victor.delahoz@gmail.com": {
        "username": "victorDhoz",
        "full_name": "victor manuel de la hoz",
        "hashed_password": "$2b$12$KIXg6eQ9a.VJjaEG1iEiqOlq5hfTymu7Mya6hQ21VZB1SxV8pXcOq",
        "disabled": False
    }
}

def get_user(db, username: str):
    """
    Busca y devuelve un usuario del diccionario simulado por nombre de usuario.
    """
    if username in db:
        return db[username]
    return None

class UserCreate(BaseModel):
    username: str
    full_name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None

    class Config:
        from_attributes = True
