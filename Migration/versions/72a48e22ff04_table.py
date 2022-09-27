"""table

Revision ID: 72a48e22ff04
Revises: 
Create Date: 2022-09-27 15:18:56.280394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72a48e22ff04'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('register',sa.Column('id',sa.Integer(),nullable=False, autoincrement=True))


def downgrade() -> None:
    op.drop_column('register','id')
