import ormar
from database.db_config import BaseMeta
from models.usuario import Usuario

class Roupa(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'roupas'

    id = ormar.Integer(primary_key=True)
    descricao = ormar.String(max_length=50)
    vendedor = ormar.ForeignKey(Usuario)
