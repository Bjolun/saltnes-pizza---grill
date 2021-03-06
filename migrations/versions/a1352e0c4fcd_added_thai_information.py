"""Added thai information

Revision ID: a1352e0c4fcd
Revises: 73ef13214b96
Create Date: 2020-04-26 01:43:40.950444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1352e0c4fcd'
down_revision = '73ef13214b96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('thai_informasjon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('thai_extra_meat', sa.String(), nullable=True),
    sa.Column('thai_extra_rice', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('thai_informasjon')
    # ### end Alembic commands ###
