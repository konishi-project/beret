from fastapi import Body
from pydantic import BaseModel, EmailStr #pylint: disable=no-name-in-module

class UserBase(BaseModel):
    email: EmailStr = Body(..., example='user@email.com')
    password: str = Body(..., example='abcd1234')

class UserRegister(UserBase):
    username: str = Body(...,
                        regex='/^([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)$/;', #pylint: disable=anomalous-backslash-in-string
                        example='user._.name'
                    )


class LoginSuccess(BaseModel):
    message: str = Body(..., example='Successfully logged in.')
    # @TODO: Add user model and jwt token.