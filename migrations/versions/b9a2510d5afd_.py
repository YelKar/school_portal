"""empty message

Revision ID: b9a2510d5afd
Revises: a9fd9f770743
Create Date: 2022-04-16 10:56:58.326147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9a2510d5afd'
down_revision = 'a9fd9f770743'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('publications', sa.Column('header', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('publications', 'header')
    # ### end Alembic commands ###
