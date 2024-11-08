import pytest
from app import db
from app.models.owner import Owner
from app.models.car import Car, ColorEnum, ModelEnum


@pytest.fixture(scope="function")
def setup(client):
    with client.application.app_context():
        owner = Owner(name="Márcio Conrado", email="marcio@conrado.com")
        db.session.add(owner)
        db.session.commit()

        car = Car(owner_id=owner.id, color=ColorEnum.YELLOW, model=ModelEnum.HATCH)
        db.session.add(car)
        db.session.commit()

        yield owner, car

        db.session.expunge(car)
        db.session.delete(car)
        db.session.expunge(owner)
        db.session.delete(owner)
        db.session.commit()


def test_get_car_not_found(client):
    response = client.get("/car/999")
    json_data = response.get_json()
    assert json_data["message"] == "Carro não encontrado."


def test_get_car(client, setup):
    owner, car = setup
    response = client.get(f"/car/{car.id}")
    json_data = response.get_json()
    assert json_data["id"] == car.id
