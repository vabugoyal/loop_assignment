"""changed models

Revision ID: 9697d0fb6941
Revises: b424586e4adb
Create Date: 2023-05-17 00:50:09.124028

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9697d0fb6941'
down_revision = 'b424586e4adb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('business_hours', 'start_time_local',
               existing_type=mysql.TIME(),
               nullable=True)
    op.alter_column('business_hours', 'end_time_local',
               existing_type=mysql.TIME(),
               nullable=True)
    op.drop_column('business_hours', 'end_time_asdfasdlocal')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('business_hours', sa.Column('end_time_asdfasdlocal', mysql.TIME(), nullable=False))
    op.alter_column('business_hours', 'end_time_local',
               existing_type=mysql.TIME(),
               nullable=False)
    op.alter_column('business_hours', 'start_time_local',
               existing_type=mysql.TIME(),
               nullable=False)
    # ### end Alembic commands ###
