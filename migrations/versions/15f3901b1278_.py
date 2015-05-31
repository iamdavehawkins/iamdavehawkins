"""empty message

Revision ID: 15f3901b1278
Revises: None
Create Date: 2015-05-31 17:24:10.870726

"""

# revision identifiers, used by Alembic.
revision = '15f3901b1278'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bikes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('img_path', sa.String(), nullable=True),
    sa.Column('retired', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('parttypes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('min_per_bike', sa.Integer(), nullable=True),
    sa.Column('max_per_bike', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('myparts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('weight_g', sa.Float(), nullable=True),
    sa.Column('color', sa.String(), nullable=True),
    sa.Column('img_path', sa.String(), nullable=True),
    sa.Column('retired', sa.Integer(), nullable=True),
    sa.Column('bike_id', sa.Integer(), nullable=True),
    sa.Column('parttype_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bike_id'], ['bikes.id'], ),
    sa.ForeignKeyConstraint(['parttype_id'], ['parttypes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('myparts')
    op.drop_table('parttypes')
    op.drop_table('bikes')
    ### end Alembic commands ###
