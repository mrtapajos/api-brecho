from http import HTTPStatus
from fastapi import APIRouter, Header, HTTPException, Depends
from JWT import get_current_user, authenticate_user, verify_token
from models.roupa import RoupaCreate
from models import Usuario, Roupa

router = APIRouter()


@router.get('/')
async def read_roupas():
    return await Roupa.objects.all()


@router.post('/')
async def create_roupa(roupa: RoupaCreate, token: str = Header(...)):
    user = await verify_token(token)

    if not user:
        raise HTTPException(HTTPStatus.BAD_REQUEST, detail='Invalid username or password!')
    
    roupa_nova = Roupa(descricao=roupa.descricao, vendedor=user)
    try:
        await roupa_nova.save()
        return {'mensagem': 'roupa criada!'}
    except Exception:
        return {'mensagem': 'erro ao criar roupa!'} 


@router.delete('/')
async def delete_roupa(roupa_id: int):
    roupa_deletada =  await Roupa.objects.get(id=roupa_id)
    try:
        await roupa_deletada.delete()
        return {'mensagem': 'roupa deletada com sucesso!'}
    except Exception:
        return {'mensagem': 'erro ao deletar roupa!'}
