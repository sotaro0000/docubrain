from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    """ルートエンドポイントの正常系テスト"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "DocuBrain Backend"}