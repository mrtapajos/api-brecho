from database.db_config import engine_handler
from models import * 
from fastapi import FastAPI, HTTPException
from routes import router
from JWT.token import authenticate_user, generate_access_token


app = FastAPI()

app.include_router(router)

@app.get('/')
def index():
    return {'mensagem': 'página existindo!'}

@app.post("/login")
async def login(user: UserCreate):
    authenticated_user = await authenticate_user(user.username, user.senha)
    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    access_token = await generate_access_token(user.username)
    return {'access token': access_token, 'token type': 'bearer'}


if __name__ == '__main__':
    engine_handler()
    print('Banco resetado!')
    