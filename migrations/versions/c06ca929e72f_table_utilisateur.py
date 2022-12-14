"""table utilisateur

Revision ID: c06ca929e72f
Revises: 
Create Date: 2022-09-07 14:52:23.461785

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c06ca929e72f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('utilisateur',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('mot_de_passe_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_utilisateur_email'), 'utilisateur', ['email'], unique=True)
    op.create_index(op.f('ix_utilisateur_nom'), 'utilisateur', ['nom'], unique=True)
    op.create_table('publications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('corps', sa.String(length=140), nullable=True),
    sa.Column('horodatages', sa.DateTime(), nullable=True),
    sa.Column('utilisateur_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['utilisateur_id'], ['utilisateur.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_publications_horodatages'), 'publications', ['horodatages'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_publications_horodatages'), table_name='publications')
    op.drop_table('publications')
    op.drop_index(op.f('ix_utilisateur_nom'), table_name='utilisateur')
    op.drop_index(op.f('ix_utilisateur_email'), table_name='utilisateur')
    op.drop_table('utilisateur')
    # ### end Alembic commands ###
