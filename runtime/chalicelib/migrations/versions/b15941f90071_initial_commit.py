"""initial commit

Revision ID: b15941f90071
Revises: 
Create Date: 2023-05-16 19:45:59.739487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b15941f90071'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('first_name', sa.String(length=128), nullable=True),
    sa.Column('last_name', sa.String(length=128), nullable=True),
    sa.Column('token', sa.String(length=128), nullable=False),
    sa.Column('ad_username', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('note',
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=4096), nullable=True),
    sa.Column('created_by_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['created_by_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('note')
    op.drop_table('user')
    # ### end Alembic commands ###