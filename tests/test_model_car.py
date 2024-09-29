import pytest
from app import app, db
from app.models.car import Car, ModelEnum, ColorEnum
from app.models.owner import Owner
from app.config import Config
from datetime import datetime

@pytest.fixture(scope='module')
def test_client():
    app.config.from_object(Config)
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()

@pytest.fixture(scope='function')
def setup_owner(test_client):
    owner = Owner(name="Márcio Conrado", email="marcio@conrado.com")
    db.session.add(owner)
    db.session.commit()
    yield owner
    db.session.delete(owner)
    db.session.commit()

@pytest.fixture(scope='function')
def setup_car(test_client, setup_owner):
    car = Car(owner_id=setup_owner.id, color=ColorEnum.BLUE, model=ModelEnum.HATCH)
    db.session.add(car)
    db.session.commit()
    yield car
    db.session.delete(car)
    db.session.commit()

def test_car_model_exists(test_client):
    assert Car is not None
    assert hasattr(Car, '__tablename__')
    assert hasattr(Car, 'id')
    assert hasattr(Car, 'owner_id')
    assert hasattr(Car, 'color')
    assert hasattr(Car, 'model')
    assert hasattr(Car, 'creation_date')

def test_car_creation(setup_car):
    assert setup_car.color in [ColorEnum.YELLOW, ColorEnum.BLUE, ColorEnum.GRAY]
    assert setup_car.model in [ModelEnum.HATCH, ModelEnum.SEDAN, ModelEnum.CONVERTIBLE]
    assert setup_car.owner_id is not None

def test_creation_date(setup_owner):
    assert isinstance(setup_owner.creation_date, datetime)

