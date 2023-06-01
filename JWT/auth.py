from http import HTTPStatus
from jose import jwt
from jwt.exceptions import PyJWTError
from fastapi import HTTPException, Depends
from models import Usuario
from JWT import oauth2_scheme, ALGORITHM, SECRET_KEY, pwd_context

# AUTENTICAÇÃO
async def authenticate_user(username: str, senha: str):
    user = await Usuario.objects.get(username=username)
    if not user:
        return False
    if not pwd_context.verify(senha, user.senha):
        return False
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if username is None:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Invalid token')
        
        user = await Usuario.get_by_username(username)
        if user is None:
            raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="Invalid user")
        return user
    except PyJWTError:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail='Invalid token')
