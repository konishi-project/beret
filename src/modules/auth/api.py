from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED

from .schemas import UserBase, UserRegister, LoginSuccess

router = APIRouter()

@router.post('/login', status_code=HTTP_200_OK, response_model=LoginSuccess)
async def login_user(credentials: UserBase):
    if not credentials:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f'Login data is required.'
        )

    # @TODO:
    # Check if the user is in the database.
    # Validate user's password
    # return

    return {
      'Unavailable': 'This resource is currently WIP.'
    }

@router.post('/register', status_code=HTTP_201_CREATED)
async def register(data: UserRegister):
    # @TODO
    # Check if the email/username is taken.
    # Create the user.
    pass