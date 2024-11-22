import pytest
from app import db
from app.models import Owner, Car
from app.models.car import ModelEnum, ColorEnum


@pytest.fixture(scope="function")
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


@pytest.fixture(scope="function")
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


def test_owner_cannot_have_more_than_three_cars(client, setup_owner, car_data):
    for i in range(3):
        Car.create_car(setup_owner.id, ColorEnum.BLUE, ModelEnum.HATCH)

    response = client.post("/car", json=car_data)

    json_data = response.get_json()
    assert "Erro ao criar carro." in json_data["message"]
