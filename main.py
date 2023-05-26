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
async def login(username: str, senha: str):
    authenticated_user = await authenticate_user(username, senha)
    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Nome de usuário ou senha inválido!")
    access_token = await generate_access_token(username)
    
    return [
        {'access token': access_token, 'token type': 'bearer'},
        {'mensagem': 'usuário acessado com sucesso!'}]


if __name__ == '__main__':
    engine_handler()
    print('Banco resetado!')
    