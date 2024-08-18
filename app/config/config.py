from main import app
from tortoise.contrib.fastapi import register_tortoise
from app.config.schemas import User
from secrets import PASSWORD, USERNAME, DB, PORT


register_tortoise(
    app,
    db_url=f"postgres://{USERNAME}:{PASSWORD}@localhost:{PORT}/{DB}",
    modules={'models': [User]},
    generate_schemas=True,
    add_exception_handlers=True,
)
