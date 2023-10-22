from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import schemas, database, models, oaut
from sqlalchemy.orm import Session
from ..repository import blog


router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)
get_db = database.get_db
get_current_user = oaut.get_current_user

@router.get('', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all(db)

@router.post('',  status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db : Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db : Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.delete(db, id)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Blog, db : Session = Depends(get_db)):
    return blog.update(db, request, id)


@router.get('/{id}', status_code=200,response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.show(db, id)