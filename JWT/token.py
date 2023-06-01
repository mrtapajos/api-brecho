from fastapi.security import OAuth2PasswordBearer
from JWT.config import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY
from passlib.context import CryptContext

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
