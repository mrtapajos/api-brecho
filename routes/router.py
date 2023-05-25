from fastapi import APIRouter

from controllers import usuario_endpoints as user

router = APIRouter()

router.include_router(user.router, prefix='/user')