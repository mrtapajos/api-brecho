from models import Usuario
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from JWT.config import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY
from passlib.context import CryptContext
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from datetime import datetime, timedelta
from jose import jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')
pwd_context = CryptContext(schemes=['bcrypt'])


# GERAR TOKEN
async def generate_access_token(username: str) -> str:

    # DEFININDO VALIDADE
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) 
    expires_at = datetime.utcnow() + expires_delta  

    # CRIPTOGRAFANDO
    to_encode: dict = {"sub": username, "exp": expires_at}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# VERIFICAR TOKEN
async def verify_token(token: str) -> Usuario:
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = decoded_token.get('sub')
        if not username:
            raise HTTPException(status_code=401, detail='Invalid token')
        
        # Perform any additional validation or retrieval of user data based on the token
        # For example, you can retrieve the user from the database based on the username
        
        user =  await Usuario.get_by_username(username)
        if not user:
            raise HTTPException(status_code=401, detail='Invalid user')
        
        return user
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token has expired')
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid token')
