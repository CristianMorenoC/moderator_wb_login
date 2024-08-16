from app.models.user import fake_users_db, get_user
from app.core.security import verify_password

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

# def create_user(username: str, password: str):

