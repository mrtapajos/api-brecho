from http import HTTPStatus
from fastapi import HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials
from models import Usuario
from .token import pwd_context, verify_token
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


security = HTTPBearer()

# AUTENTICAÇÃO
async def authenticate_user(username: str, senha: str):
    user = await Usuario.objects.get(username=username)
    if not user:
        return False
    if not pwd_context.verify(senha, user.senha):
        return False
    return user


# ACESSAR USUÁRIO
async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:  
        token = credentials.credentials
        print(f'Token: {token}')
        username = verify_token(token)  # Verify and decode the token

        # PEGAR USUARIO PELO USERNAME
        user = await Usuario.get_by_username(username)
        if user is None:
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail='Invalid user')
        return user
    except HTTPException as e:
        raise e
