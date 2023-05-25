import ormar
from database.db_config import BaseMeta

class Usuario(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'usuarios'

    id = ormar.Integer(primary_key=True, auto_increment=True)
    username = ormar.String(max_length=50)
    senha = ormar.String(max_length=50)
    livros = ormar.Integer(nullable=True)
    papel = ormar.String(max_length=10)
