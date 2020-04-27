"""updated database to include pizza info

Revision ID: 73ef13214b96
Revises: f255f77a6484
Create Date: 2020-04-26 01:08:23.801971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73ef13214b96'
down_revision = 'f255f77a6484'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pizza_informasjon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('medium_pizza_price', sa.Integer(), nullable=True),
    sa.Column('price_red_sauce', sa.Integer(), nullable=True),
    sa.Column('price_white_sauce', sa.Integer(), nullable=True),
    sa.Column('pizza_extra_meat', sa.Integer(), nullable=True),
    sa.Column('pizza_extra_cheese', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('medium_pizza')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('medium_pizza',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('medium_pizza', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('pizza_informasjon')
    # ### end Alembic commands ###