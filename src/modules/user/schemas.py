from fastapi import Body
from typing import Optional
from pydantic import BaseModel #pylint: disable=no-name-in-module

class UserBase(BaseModel):
    email: str
    username: str
    fullName: Optional[str]

class DeleteResponse(BaseModel):
    message: str = Body(..., example='User set for deletion, it will now be no longer available.')
