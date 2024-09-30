import pytest
from app import app, db
from app.models.owner import Owner
from app.config import Config
from datetime import datetime
from app.validators import is_valid_email

@pytest.fixture(scope='module')
def test_client():
    app.config.from_object(Config)
    app.config['TESTING'] = True
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

def test_owner_model_exists(test_client):
    assert Owner is not None
    assert hasattr(Owner, '__tablename__')
    assert hasattr(Owner, 'id')
    assert hasattr(Owner, 'name')
    assert hasattr(Owner, 'email')
    assert hasattr(Owner, 'sales_o')
    assert hasattr(Owner, 'creation_date')

def test_creation_date(setup_owner):
    assert isinstance(setup_owner.creation_date, datetime)

def test_sales_opportunity_default_to_False(setup_owner):
    assert setup_owner.sales_o == False

def test_email_field_is_email(setup_owner):
    assert is_valid_email(setup_owner.email)
