import pytest
from app import app, db
from app.config import Config

@pytest.fixture
def client():
    app.config.from_object(Config)
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  
        yield client
        with app.app_context():
            db.drop_all()

