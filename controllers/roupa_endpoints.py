from http import HTTPStatus
from fastapi import APIRouter, Header, HTTPException
from JWT import get_current_user, authenticate_user
from models.roupa import RoupaCreate
from models import Usuario, Roupa

router = APIRouter()

@router.post('/')
async def create_roupa(roupa: RoupaCreate, username: str = Header(...), password: str = Header(...)):
    user = await authenticate_user(username, password)
    if not user:
        raise HTTPException(HTTPStatus.BAD_REQUEST, detail='Invalid username or password!')
    
    roupa_nova = Roupa(descricao=roupa.descricao, vendedor=user)
    try:
        await roupa_nova.save()
        return {'mensagem': 'roupa criada!'}
    except Exception:
        return {'mensagem': 'erro ao criar roupa!'}


