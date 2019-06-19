"""empty message

Revision ID: b48f52083ee1
Revises: 
Create Date: 2019-06-18 11:49:25.051494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b48f52083ee1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grillmenu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('allergies', sa.String(), nullable=True),
    sa.Column('price_small', sa.String(), nullable=True),
    sa.Column('price_medium', sa.String(), nullable=True),
    sa.Column('price_large', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pizzamenu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('allergies', sa.String(), nullable=True),
    sa.Column('price', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('thaimenu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('allergies', sa.String(), nullable=True),
    sa.Column('price', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('thaimenu')
    op.drop_table('pizzamenu')
    op.drop_table('grillmenu')
    # ### end Alembic commands ###