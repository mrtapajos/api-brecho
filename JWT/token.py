# from main import app    
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer, HTTPBearer
from models import Usuario, UserCreate
from controllers.usuario_endpoints import pwd_context
from JWT.config import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY

from datetime import datetime, timedelta
from jose import jwt, JWTError
from database.db_config import database


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')


# AUTENTICAÇÃO
async def authenticate_user(username: str, senha: str):
    user = await Usuario.objects.get(username=username)
    if not user:
        return False
    if not pwd_context.verify(senha, user.senha):
        return False
    return user


# CRIAR TOKEN
# async def create_access_token(data: dict, expire_delta: timedelta):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + expire_delta
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt


# GERAR TOKEN
async def generate_access_token(username: str):

    # DEFININDO VALIDADE
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) 
    expires_at = datetime.utcnow() + expires_delta  

    # CRIPTOGRAFANDO
    to_encode: dict = {"sub": username, "exp": expires_at}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
