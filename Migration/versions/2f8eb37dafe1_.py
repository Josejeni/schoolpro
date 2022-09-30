"""empty message

Revision ID: 2f8eb37dafe1
Revises: 
Create Date: 2022-09-29 15:01:09.645723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f8eb37dafe1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
     op.create_table('register',sa.Column('username',sa.String(),nullable = False,primary_key=True))


def downgrade() -> None:
    pass
