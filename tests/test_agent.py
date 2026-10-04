from fastapi.testclient import TestClient
from agentx.main import app
client = TestClient(app)

def test_run_and_refuse():
    payload = client.post("/agent/run", json={"goal": 'add a healthz test', "payload": {}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert "add test" in payload["plan"]
    refused = client.post("/agent/run", json={"goal": 'git push origin main'}).json()
    assert refused["refused"] is True
