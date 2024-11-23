import pytest
from app import db
from app.models.car import Car, ModelEnum, ColorEnum
from app.models.owner import Owner
from datetime import datetime


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
def setup_car(client, setup_owner):
    with client.application.app_context():
        car = Car(owner_id=setup_owner.id, color=ColorEnum.BLUE, model=ModelEnum.HATCH)
        db.session.add(car)
        db.session.commit()
        yield car
        db.session.delete(car)
        db.session.commit()


def test_car_model_exists():
    assert Car is not None
    assert hasattr(Car, "__tablename__")
    assert hasattr(Car, "id")
    assert hasattr(Car, "owner_id")
    assert hasattr(Car, "color")
    assert hasattr(Car, "model")
    assert hasattr(Car, "creation_date")


def test_car_creation(setup_car):
    assert setup_car.color in [ColorEnum.YELLOW, ColorEnum.BLUE, ColorEnum.GRAY]
    assert setup_car.model in [ModelEnum.HATCH, ModelEnum.SEDAN, ModelEnum.CONVERTIBLE]
    assert setup_car.owner_id is not None


def test_creation_date(setup_car):
    assert isinstance(setup_car.creation_date, datetime)


def test_not_more_than_three_cars_per_owner(setup_owner):
    for _ in range(3):
        Car.create_car(setup_owner.id, ColorEnum.BLUE, ModelEnum.HATCH)

    with pytest.raises(Exception) as excinfo:
        Car.create_car(setup_owner.id, ColorEnum.YELLOW, ModelEnum.SEDAN)

    assert str(excinfo.value) == "Um proprietário não pode ter mais de 3 carros."
