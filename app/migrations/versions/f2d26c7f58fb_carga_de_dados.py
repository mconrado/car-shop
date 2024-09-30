"""carga de dados

Revision ID: f2d26c7f58fb
Revises: 11a6a4898158
Create Date: 2024-09-30 20:09:04.165358

"""
from alembic import op
import sqlalchemy as sa
from app.models import Owner, Car
from app.models.car import ColorEnum, ModelEnum


# revision identifiers, used by Alembic.
revision = 'f2d26c7f58fb'
down_revision = '11a6a4898158'
branch_labels = None
depends_on = None

def upgrade():
    # Inserir dados de owners
    conn = op.get_bind()
    conn.execute(
        Owner.__table__.insert(),
        [
            {"name": "João", "email": "joao@carlos", "sales_o": False},
            {"name": "Maria", "email": "maria@joaquina.com", "sales_o": False},
            {"name": "José", "email": "jose@roberto.com", "sales_o": True},
        ]
    )

    # Inserir dados de cars
    conn.execute(
        Car.__table__.insert(),
        [
            {"owner_id": 1, "color": ColorEnum.YELLOW.value, "model": ModelEnum.HATCH.value},
            {"owner_id": 1, "color": ColorEnum.BLUE.value, "model": ModelEnum.SEDAN.value},
            {"owner_id": 1, "color": ColorEnum.GRAY.value, "model": ModelEnum.CONVERTIBLE.value},
            {"owner_id": 2, "color": ColorEnum.YELLOW.value, "model": ModelEnum.SEDAN.value},
            {"owner_id": 2, "color": ColorEnum.BLUE.value, "model": ModelEnum.HATCH.value},
        ]
    )

def downgrade():
    # Remover dados de cars
    conn = op.get_bind()
    conn.execute(Car.__table__.delete())
    
    # Remover dados de owners
    conn.execute(Owner.__table__.delete())
