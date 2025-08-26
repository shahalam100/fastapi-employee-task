from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import UserRead
from ..models import User
from ..deps import get_current_user

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=UserRead)
def read_me(current: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return current
