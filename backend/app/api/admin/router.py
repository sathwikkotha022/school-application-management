from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserOut
from app.crud.user import get_all_users
from app.api.auth.router import get_current_user  # <- use the correct function

router = APIRouter(tags=["Admin"])

@router.get("/users", response_model=list[UserOut])
def list_users(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    # Optional: add role check here
    return get_all_users(db)
