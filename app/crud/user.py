from app.models.user import fake_users_db, get_user
from app.core.security import verify_password
from app.models.user import UserCreate, UserResponse
from passlib.context import CryptContext
from app.config.schemas.user import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def authenticate_user(username: str, password: str):
    """
    Autentica al usuario verificando la contraseña y el nombre de usuario.
    """
    user = get_user(fake_users_db, username)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
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