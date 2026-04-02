from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.schemas.user import User, UserCreate
from app.services import user

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/", response_model=User)
def create_user_endpoint(user_data: UserCreate, db: Session = Depends(get_db)):
    return user.create_user(db=db, user=user_data)
