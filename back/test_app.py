from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_zero_threshold():
    response = client.get('/test/?percentage_threshold=0&euro_threshold=0')
    assert response.status_code == 200
    assert response.json() == {'1':70, '2':790, '3':30, '4':30, '5':1, '6':599500, '7':2, '8':3, '9':89500, '10':100}

def test_zero_threshold_last_two():
    response = client.get('/test/?percentage_threshold=0&euro_threshold=0&last_two=true')
    assert response.status_code == 200
    assert response.json() == {'1': 69, '2': 789, '3': 0, '4': 0, '5': 989, '6': 599498, '7': 0, '8': 97, '9': 89100, '10': 400}

def test_threshold():
    response = client.get('/test/?percentage_threshold=100000&euro_threshold=800')
    assert response.status_code == 200
    assert response.json() == {'6': 599500,'9': 89500}

def test_threshold_last_two():
    response = client.get('/test/?percentage_threshold=100000&euro_threshold=800&last_two=true')
    assert response.status_code == 200
    assert response.json() == {'5': 989,'6': 599498,'9': 89100}

def test_high_threshold():
    response = client.get('/test/?percentage_threshold=1000&euro_threshold=1000')
    assert response.status_code == 200
    assert response.json() == {'2': 790, '6': 599500, '9': 89500}

def test_high_threshold_last_two():
    response = client.get('/test/?percentage_threshold=1000&euro_threshold=1000&last_two=true')
    assert response.status_code == 200
    assert response.json() == {'2': 789, '6': 599498, '9': 89100}
