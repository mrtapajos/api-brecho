from http import HTTPStatus
from fastapi import APIRouter, HTTPException
from models.usuario import Usuario
from JWT import pwd_context, generate_access_token, authenticate_user
from models.usuario import UserCreate

router = APIRouter()

@router.get('/')
async def read_users():
    return await Usuario.objects.all()
    

@router.post('/register', response_model=Usuario)
async def register(user: UserCreate) -> Usuario:
    hashed_password = pwd_context.hash(user.senha)
    new_user = Usuario(
        username=user.username,
        senha=hashed_password,
        papel=user.papel)
    await new_user.save()
    return new_user


@router.post("/login")
async def login(username: str, senha: str):
    authenticated_user = await authenticate_user(username, senha)
    if not authenticated_user:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Nome de usuário ou senha inválido!")
    access_token = await generate_access_token(username)
    
    return [
        {'access token': access_token, 'token type': 'bearer'},
        {'mensagem': 'usuário acessado com sucesso!'}]