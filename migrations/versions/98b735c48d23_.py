"""empty message

Revision ID: 98b735c48d23
Revises: 3669617b1a02
Create Date: 2022-04-16 13:26:53.249565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98b735c48d23'
down_revision = '3669617b1a02'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('publications', sa.Column('type', sa.String(length=15), nullable=True))
    op.drop_column('publications', 'is_event')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('publications', sa.Column('is_event', sa.BOOLEAN(), nullable=True))
    op.drop_column('publications', 'type')
    # ### end Alembic commands ###