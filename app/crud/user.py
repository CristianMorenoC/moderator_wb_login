from app.core.security import verify_password
from app.models.user import UserCreate, UserResponse
from passlib.context import CryptContext
from app.config.schemas.user import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def authenticate_user(username: str, password: str):
    """
    Autentica al usuario verificando la contraseña y el nombre de usuario.
    """
    user = await get_user(username)
    print("user:", user)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

def get_password_hash(password):
    return pwd_context.hash(password)

async def create_user(user: UserCreate) -> UserResponse:
    """crea un nuevo usuario"""
    hashed_password = get_password_hash(user.password)
    user_obj = await User.create(
        username= user.username,
        full_name= user.full_name,
        email= user.email,
        password= hashed_password
    )
    return UserResponse.from_orm(user_obj)

async def get_all_users():
    users = await User.all()
    if not users:
        return False
    return users

async def get_user(username):
    user= await User.get(username=username)
    if not user:
        return False
    return user
    