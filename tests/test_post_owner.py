import pytest


@pytest.fixture
def owner_data():
    return {
        "name": "Márcio Conrado",
        "email": "marcio@conrado.com"
    }

def test_create_owner(client, owner_data):
    response = client.post('/owner', json=owner_data)
    assert response.status_code == 201
    
def test_return_is_json(client, owner_data):
    response = client.post('/owner', json=owner_data)
    assert response.is_json


def test_wrong_email(client, owner_data):
    owner_data['email'] = "marcio@conrado"
    
    response = client.post('/owner', json=owner_data)
    json_data = response.get_json()
    assert 'Email inválido' in json_data["message"]
