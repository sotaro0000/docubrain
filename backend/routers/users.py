from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from schemas.user import UserCreate, UserResponse

router = APIRouter()

@router.post("/users/",response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    #1. 同じメールアドレスのユーザーがいないか確認
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    #2. ユーザーモデルの作成(パスワードハッシュ化)
    new_user = User(email=user.email,password=user.password)
    
    #3. DBへの保存
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user