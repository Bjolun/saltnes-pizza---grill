"""added misc information to the db

Revision ID: ac03049f185c
Revises: b71c4f6c2107
Create Date: 2020-04-25 23:33:24.696471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac03049f185c'
down_revision = 'b71c4f6c2107'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('informasjon',
    sa.Column('info_number', sa.Integer(), nullable=False),
    sa.Column('medium_pizza', sa.Integer(), nullable=True),
    sa.Column('red_sauce', sa.Integer(), nullable=True),
    sa.Column('white_sauce', sa.Integer(), nullable=True),
    sa.Column('pizza_extra_meat', sa.Integer(), nullable=True),
    sa.Column('pizza_extra_cheese', sa.Integer(), nullable=True),
    sa.Column('thai_extra_meat', sa.Integer(), nullable=True),
    sa.Column('thai_extra_rice', sa.Integer(), nullable=True),
    sa.Column('front_page_text', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('info_number')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('informasjon')
    # ### end Alembic commands ###
