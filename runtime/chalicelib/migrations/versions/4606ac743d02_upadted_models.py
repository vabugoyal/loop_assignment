"""upadted models

Revision ID: 4606ac743d02
Revises: c518d598f6bc
Create Date: 2023-05-19 22:32:05.950690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4606ac743d02'
down_revision = 'c518d598f6bc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('report_results',
    sa.Column('report_id', sa.Integer(), nullable=False),
    sa.Column('store_id', sa.String(length=128), nullable=False),
    sa.Column('uptime_last_hour', sa.Integer(), nullable=True),
    sa.Column('downtime_last_hour', sa.Integer(), nullable=True),
    sa.Column('uptime_last_day', sa.Integer(), nullable=True),
    sa.Column('downtime_last_day', sa.Integer(), nullable=True),
    sa.Column('uptime_last_week', sa.Integer(), nullable=True),
    sa.Column('downtime_last_week', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('report_id', 'store_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('report_results')
    # ### end Alembic commands ###
