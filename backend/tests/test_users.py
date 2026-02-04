from fastapi.testclient import TestClient

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
from main import app

# from database import Base
from database import get_db
# from models.user import User

# テスト用DB
client = TestClient(app)


def test_create_user():
    # 1. 準備：テストデータ
    user_data = {"email": "test@example.com", "password": "password1123"}

    # 2. 実行：APIをたたく
    response = client.post("/users/", json=user_data)

    # 3. 検証(アサーション)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == user_data["email"]
    assert "id" in data
    assert "password" not in data  # パスワードをレスポンスに含まない
