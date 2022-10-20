"""table utilisateur

Revision ID: 4fcfb6bc8607
Revises: c06ca929e72f
Create Date: 2022-09-07 14:53:54.088875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fcfb6bc8607'
down_revision = 'c06ca929e72f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_publications_horodatages', table_name='publications')
    op.drop_table('publications')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('publications',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('corps', sa.VARCHAR(length=140), nullable=True),
    sa.Column('horodatages', sa.DATETIME(), nullable=True),
    sa.Column('utilisateur_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['utilisateur_id'], ['utilisateur.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_publications_horodatages', 'publications', ['horodatages'], unique=False)
    # ### end Alembic commands ###
