import pytest
from app import create_app, db
from models import Owner

@pytest.fixture
def app():
    app = create_app('testing')  # Certifique-se de ter uma configuração de teste
    with app.app_context():
        db.create_all()  # Cria todas as tabelas
        yield app
        db.drop_all()  # Remove todas as tabelas após os testes

@pytest.fixture
def client(app):
    return app.test_client()

def test_owner_model_exists(app):
    # Verifica se a model Owner existe
    owner = Owner(name='Test Owner', email='test@example.com', sales_opportunity=True)
    db.session.add(owner)
    db.session.commit()

    # Verifica se o owner foi adicionado ao banco de dados
    assert owner.id is not None  # O ID deve ser gerado
    assert owner.name == 'Test Owner'  # Verifica o nome
    assert owner.email == 'test@example.com'  # Verifica o email
    assert owner.sales_opportunity is True  # Verifica a oportunidade de venda

