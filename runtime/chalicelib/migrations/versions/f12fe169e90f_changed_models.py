"""changed models

Revision ID: f12fe169e90f
Revises: 5e086526c6ad
Create Date: 2023-05-17 02:02:49.283527

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f12fe169e90f'
down_revision = '5e086526c6ad'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('store', sa.Column('store_id', sa.String(length=128), nullable=False))
    op.drop_column('store', 'id')
    op.add_column('stores_status', sa.Column('timestamp', sa.Time(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stores_status', 'timestamp')
    op.add_column('store', sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False))
    op.drop_column('store', 'store_id')
    # ### end Alembic commands ###