import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#環境変数からDB　URLを取得
DATABASE_URL = os.getenv(
    "DATABASE_URL","postgresql://user:password@localhost:5432/docubrain_db"
)

# エンジンの作成
engine = create_engine(DATABASE_URL)

# セッションの作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# モデルのベースクラス
Base = declarative_base()

# DBセッションを取得する依存関係
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        