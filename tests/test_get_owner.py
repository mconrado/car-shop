import pytest
from app import db
from app.models.owner import Owner


@pytest.fixture(scope="function")
def setup_owner(client):
    with client.application.app_context():
        owner = Owner(name="Márcio Conrado", email="marcio@conrado.com")
        db.session.add(owner)
        db.session.commit()
        yield owner
        db.session.delete(owner)
        db.session.commit()


def test_get_owner_not_found(client):
    response = client.get("/owner/999")
    json_data = response.get_json()
    assert json_data["message"] == "Proprietário não encontrado."


def test_get_owner(client, setup_owner):
    response = client.get(f"/owner/{setup_owner.id}")
    json_data = response.get_json()
    assert json_data["id"] == setup_owner.id
