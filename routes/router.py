from fastapi import APIRouter

from controllers import usuario_endpoints as user, roupa_endpoints as roupa

router = APIRouter()

router.include_router(user.router, prefix='/user')
router.include_router(roupa.router, prefix='/roupa')