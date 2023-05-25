import databases
import sqlalchemy
import ormar


DATABASE_URL = 'sqlite:///database/database.sqlite'
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database

def engine_handler() -> None:
    engine = sqlalchemy.create_engine(DATABASE_URL)
    metadata.drop_all(engine)
    metadata.create_all(engine)

