from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_health():
    r = client.get('/api/v1/health')
    assert r.status_code == 200 and r.json()['status'] == 'ok'

def test_models():
    r = client.get('/api/v1/models')
    assert r.status_code == 200
    assert set(r.json()['hydraulic']) == {'cooler','valve','pump','accumulator'}

def test_reject_invalid_kind():
    r = client.post('/api/v1/predict/csv?kind=wrong&target=cooler', files={'file':('data.csv',b'x,y\n1,2\n','text/csv')})
    assert r.status_code == 422

def test_reject_wrong_extension():
    r = client.post('/api/v1/predict/csv?kind=hydraulic&target=cooler', files={'file':('data.txt',b'x,y\n1,2\n','text/plain')})
    assert r.status_code == 415
