from typing import Dict
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from . import model, crud
from src.middleware.orm import SessionLocal, engine

model.Base.metadata.create_all(engine)

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() #pylint: disable=no-member

@router.get("/{username}", status_code=200)
async def load_user(username: str, db: Session = Depends(get_db)):
    user = crud.get_user(db, username)

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
async def remove_user(email: str, db: Session = Depends(get_db)):
    user = crud.delete_user(db, email)

    if not user:
        raise HTTPException(
            status_code=404,
            detail=f'User <{ email }> not found.'
        )
    return {
        'message': f'User <{ email }> has been deleted!'
    }