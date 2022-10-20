"""empty message

Revision ID: ac2ba100c9c9
Revises: 3d952606eed1
Create Date: 2022-10-19 14:00:10.699100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac2ba100c9c9'
down_revision = '3d952606eed1'
branch_labels = None
depends_on = None


def upgrade():
    #op.drop_column('utilisateur', 'mot_de_passe')
    pass
def downgrade():
    pass
