from fastapi import APIRouter, Depends, HTTPException, status
from .. import database, models, schemas, hashing
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db
Hash = hashing.Hash


@router.post('', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(db, request)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.find(db, id)