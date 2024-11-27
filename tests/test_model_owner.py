import pytest
from app import db
from app.models.owner import Owner
from app.models.car import Car, ModelEnum, ColorEnum
from datetime import datetime
from app.validators import is_valid_email


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


def test_owner_model_exists():
    assert Owner is not None
    assert hasattr(Owner, "__tablename__")
    assert hasattr(Owner, "id")
    assert hasattr(Owner, "name")
    assert hasattr(Owner, "email")
    assert hasattr(Owner, "sales_o")
    assert hasattr(Owner, "creation_date")


def test_creation_date(setup_owner):
    assert isinstance(setup_owner.creation_date, datetime)


def test_new_owner_must_be_sales_opportunity(setup_owner):
    """new owner have no car, hence owner must be sales opportunity"""
    assert setup_owner.sales_o == True


def test_owner_with_car_should_not_be_sales_opportunity(setup_owner):
    """owner with car must be sales opportunity equal False"""
    Car.create_car(setup_owner.id, ColorEnum.BLUE, ModelEnum.HATCH)
    assert setup_owner.sales_o == False


def test_owner_without_car_must_be_sales_opportunity(setup_owner):
    """owner without car must change to sales opportunity equal True"""
    car = Car.create_car(setup_owner.id, ColorEnum.BLUE, ModelEnum.HATCH)

    # print(db.session.get(Car, car.id))

    db.session.delete(car)
    db.session.commit()

    # print(db.session.get(Car, car.id))

    assert setup_owner.sales_o == True


def test_email_field_is_email(setup_owner):
    assert is_valid_email(setup_owner.email)
