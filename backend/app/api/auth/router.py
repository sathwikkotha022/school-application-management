from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserOut, UserCreate
from app.crud.user import create_user, get_user_by_email
from app.database import get_db
from app.core.security import create_access_token, verify_password
from fastapi.security import OAuth2PasswordBearer
from app.models.user import User
oauth2_scheme_user = OAuth2PasswordBearer(tokenUrl="/auth/login")

router = APIRouter(tags=["Auth"])
def get_current_user(token: str = Depends(oauth2_scheme_user), db: Session = Depends(get_db)) -> User:
    # Dummy example: replace with real token verification
    user = db.query(User).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid authentication")
    return user
@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user)

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token({"user_id": user.id})
    return {"access_token": token, "token_type": "bearer"}
