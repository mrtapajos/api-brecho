from database.db_config import engine_handler
from models import * 
from fastapi import FastAPI
from routes import router

app = FastAPI()

app.include_router(router)


if __name__ == '__main__':
    engine_handler()
    