"""first

Revision ID: 54be99e0ad13
Revises: 
Create Date: 2019-04-22 22:09:42.128568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54be99e0ad13'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('photos', sa.ARRAY(sa.LargeBinary(length=102400)), nullable=True),
    sa.Column('photos_filename', sa.ARRAY(sa.String()), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('first_name'),
    sa.UniqueConstraint('last_name'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
