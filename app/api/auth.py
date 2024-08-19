from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from tortoise.exceptions import DoesNotExist
from typing import List
from datetime import timedelta
from app.crud.user import authenticate_user, create_user, get_all_users
from app.core.security import create_access_token, decode_access_token
from app.models.user import UserCreate, UserResponse
from app.crud.user import get_user

# Define un router para las rutas de autenticación
router = APIRouter()

# Dependencia para la obtención de tokens OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/users", response_model=List[UserResponse])
async def get_users(token: str = Depends(oauth2_scheme)):
    """Ruta para obtener la lista de todos los usuarios"""
    print("hola mundo")
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    username = decode_access_token(token)
    print(username)
    if username is None:
        raise credentials_exception
    try:
        users=await get_all_users()
        return users
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_4014_NOT_FOUND,
            detail="There are not users"
        )



@router.post("/token", response_model=dict)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
     Ruta para el inicio de sesión y generación de un token JWT.
    """
    user = await authenticate_user(form_data.username, form_data.password)
    print(form_data)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me", response_model=UserResponse)
async def read_user_me(token: str = Depends(oauth2_scheme)):
    """
    Ruta para obtener el usuario autenticado
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    username= decode_access_token(token)
    if username is None:
        raise credentials_exception
    user = await get_user(username)
    return user



@router.post("/users")
async def register_user(user: UserCreate):
    print(user)
    return await create_user(user)