"""Novos owners devem vir como sales_o = true

Revision ID: 49ddb4a94078
Revises: f2d26c7f58fb
Create Date: 2024-11-26 23:08:53.362462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49ddb4a94078'
down_revision = 'f2d26c7f58fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('owners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('sales_o', sa.Boolean(), nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('cars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('color', sa.Enum('YELLOW', 'BLUE', 'GRAY', name='colorenum'), nullable=False),
    sa.Column('model', sa.Enum('HATCH', 'SEDAN', 'CONVERTIBLE', name='modelenum'), nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['owners.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cars')
    op.drop_table('owners')
    # ### end Alembic commands ###