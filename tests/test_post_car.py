import pytest
from app import db
from app.models import Owner, Car


@pytest.fixture
def setup_owner(client):
    with client.application.app_context():
        owner = Owner(name="Márcio Conrado", email="marcio@conrado.com")
        db.session.add(owner)
        db.session.commit()
        yield owner
        Car.query.filter_by(owner_id=owner.id).delete()
        db.session.delete(owner)
        db.session.commit()
    return owner


@pytest.fixture
def car_data(setup_owner):
    return {
        "owner_id": setup_owner.id,
        "color": "yellow",
        "model": "hatch",
    }


def test_create_car(client, car_data):
    response = client.post("/car", json=car_data)
    assert response.status_code == 201


def test_invalid_color(client, car_data):
    car_data["color"] = "invalid_color"

    response = client.post("/car", json=car_data)
    assert response.status_code == 500

    db.session.rollback()


def test_invalid_model(client, car_data):
    car_data["model"] = "invalid_model"

    response = client.post("/car", json=car_data)
    assert response.status_code == 500

    db.session.rollback()


def test_missing_owner_id(client, car_data):
    del car_data["owner_id"]
    response = client.post("/car", json=car_data)
    json_data = response.get_json()
    assert "Owner ID, cor e modelo são obrigatórios." in json_data["message"]
