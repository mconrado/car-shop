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


@pytest.fixture(scope="function")
def setup_car(setup_owner):
    return {
        "owner_id": setup_owner.id,
        "color": "yellow",
        "model": "hatch",
    }


def test_create_car(client, setup_car):
    response = client.post("/car", json=setup_car)
    assert response.status_code == 201


def test_invalid_color(client, setup_car):
    setup_car["color"] = "invalid_color"

    response = client.post("/car", json=setup_car)
    assert response.status_code == 500

    db.session.rollback()


def test_invalid_model(client, setup_car):
    setup_car["model"] = "invalid_model"

    response = client.post("/car", json=setup_car)
    assert response.status_code == 500

    db.session.rollback()


def test_missing_owner_id(client, setup_car):
    del setup_car["owner_id"]
    response = client.post("/car", json=setup_car)
    json_data = response.get_json()
    assert "Owner ID, cor e modelo são obrigatórios." in json_data["message"]


def test_owner_cannot_have_more_than_three_cars(client, setup_car):
    for _ in range(3):
        Car.create_car(setup_car["owner_id"], ColorEnum.BLUE, ModelEnum.HATCH)

    response = client.post("/car", json=setup_car)

    json_data = response.get_json()
    assert "Erro ao criar carro." in json_data["message"]
