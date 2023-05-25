from fastapi import APIRouter
from models.usuario import Usuario
from passlib.context import CryptContext
from models.usuario import UserCreate

router = APIRouter()

@router.get('/')
async def read_users():
    return await Usuario.objects.all()
    
pwd_context = CryptContext(schemes=['bcrypt'])

@router.post('/register', response_model=Usuario)
async def register(user: UserCreate) -> Usuario:
    hashed_password = pwd_context.hash(user.senha)
    new_user = Usuario(
        username=user.username,
        senha=hashed_password,
        livros=user.livros,
        papel=user.papel)
    await new_user.save()
    return new_user