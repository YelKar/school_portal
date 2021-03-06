"""empty message

Revision ID: 3669617b1a02
Revises: b9a2510d5afd
Create Date: 2022-04-16 13:11:41.844708

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3669617b1a02'
down_revision = 'b9a2510d5afd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('publications', sa.Column('is_event', sa.Boolean(), nullable=True))
    op.add_column('publications', sa.Column('date', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('publications', 'date')
    op.drop_column('publications', 'is_event')
    # ### end Alembic commands ###
