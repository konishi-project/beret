from typing import Dict
from fastapi import APIRouter, HTTPException, Depends

from . import crud

router = APIRouter()

@router.get("/{username}", status_code=200)
async def load_user(username: str):
    user = crud.get_user(username)

    if not user:
        raise HTTPException(
            status_code=404,
            detail=f'User <{ username }> not found.'
        )

    data: Dict[str, str] = {
        'message': 'User data sent',
        'user': user
    }

    return data

@router.delete("/{email}", status_code=200)
async def remove_user(email: str):
    user = crud.delete_user(email)

    if not user:
        raise HTTPException(
            status_code=404,
            detail=f'User <{ email }> not found.'
        )
    return {
        'message': f'User <{ email }> has been deleted!'
    }