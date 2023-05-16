"""added store

Revision ID: f50fc4613c46
Revises: b15941f90071
Create Date: 2023-05-16 23:23:54.204607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f50fc4613c46'
down_revision = 'b15941f90071'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('business_hours',
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('store_id', sa.Integer(), nullable=False),
    sa.Column('dayOfWeek', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('store_id', 'dayOfWeek')
    )
    op.create_table('store',
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stores_status',
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('store_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('store_id')
    )
    op.create_table('time_zone',
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('store_id', sa.Integer(), nullable=False),
    sa.Column('time_zone', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('store_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('time_zone')
    op.drop_table('stores_status')
    op.drop_table('store')
    op.drop_table('business_hours')
    # ### end Alembic commands ###