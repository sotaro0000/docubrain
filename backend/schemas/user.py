from pydantic import BaseModel, EmailStr

# ユーザー作成時の入力データ(パスワード必須)
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
# ユーザー情報の返却データ(パスワードは返さない)
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    
    class Config:
        from_attributes = True
        