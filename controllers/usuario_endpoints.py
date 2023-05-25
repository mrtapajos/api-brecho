from fastapi import APIRouter
from models.usuario import Usuario

router = APIRouter()

@router.get('/')
async def read_users():
    return await Usuario.objects.all()
    
