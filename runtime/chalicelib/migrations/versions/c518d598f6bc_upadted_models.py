"""upadted models

Revision ID: c518d598f6bc
Revises: 727ed7149c2c
Create Date: 2023-05-19 22:30:20.551487

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c518d598f6bc'
down_revision = '727ed7149c2c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('report_results', 'uptime_last_hour',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('report_results', 'downtime_last_hour',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('report_results', 'uptime_last_day',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('report_results', 'downtime_last_day',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('report_results', 'uptime_last_week',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('report_results', 'downtime_last_week',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('report_results', 'downtime_last_week',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('report_results', 'uptime_last_week',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('report_results', 'downtime_last_day',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('report_results', 'uptime_last_day',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('report_results', 'downtime_last_hour',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('report_results', 'uptime_last_hour',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    # ### end Alembic commands ###