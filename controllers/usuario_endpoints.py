from fastapi import APIRouter
from models.usuario import Usuario

router = APIRouter()

@router.get('/')
async def read_users():
    return await Usuario.objects.all()
    

@router.post('/')
async def create_user(usuario: Usuario) -> dict:
    await usuario.save()
    return {'mensagem': 'usuário criado!'}

@router.delete('/')
async def delete_user(usuario_id: int) -> dict:
    usuario =  await Usuario.objects.get(id=usuario_id)
    await usuario.delete()
    return {'mensagem': 'usuário deletado com sucesso!'}