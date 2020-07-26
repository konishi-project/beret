from typing import Dict
from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from . import crud
from .schemas import DeleteResponse

router = APIRouter()

@router.get("/{username}", status_code=200)
async def load_user(username: str):
    user = crud.get_user(username)

    if not user:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=f'User <{ username }> not found.'
        )

    ret: Dict[str, str] = {
        'message': 'User data sent',
        'user': user
    }

    return ret

@router.delete("/{email}", status_code=200, response_model=DeleteResponse)
async def remove_user(email: str):
    user = crud.delete_user(email)

    if not user:
        raise HTTPException(
            status_code=404,
            detail=f'User <{ email }> not found.'
        )

    ret: Dict[str, str] = {
        'message': f'User <{ email }> set for deletion, it will now be no longer available.'
    }

    return ret