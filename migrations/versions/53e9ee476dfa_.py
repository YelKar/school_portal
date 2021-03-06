"""empty message

Revision ID: 53e9ee476dfa
Revises: 98b735c48d23
Create Date: 2022-04-16 20:42:38.978455

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53e9ee476dfa'
down_revision = '98b735c48d23'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('publications', sa.Column('publication_date', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('publications', 'publication_date')
    # ### end Alembic commands ###
