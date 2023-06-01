import ormar
from database.db_config import BaseMeta
from pydantic import BaseModel

class Usuario(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'usuarios'

    id = ormar.Integer(primary_key=True, auto_increment=True)
    username = ormar.String(max_length=50)
    senha = ormar.String(max_length=200)
    papel = ormar.String(max_length=10)

    @classmethod
    async def get_by_username(cls, username: str):
        return await cls.objects.get(username=username)


class UserCreate(BaseModel):
    username: str
    senha: str
    papel: str
