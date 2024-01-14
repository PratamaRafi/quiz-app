"""Initial migration

Revision ID: 409290e0b2e6
Revises: 
Create Date: 2024-01-14 14:50:48.850733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '409290e0b2e6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
    sa.Column('q_id', sa.Integer(), nullable=False),
    sa.Column('ques', sa.String(length=350), nullable=True),
    sa.Column('a', sa.String(length=100), nullable=True),
    sa.Column('b', sa.String(length=100), nullable=True),
    sa.Column('c', sa.String(length=100), nullable=True),
    sa.Column('d', sa.String(length=100), nullable=True),
    sa.Column('ans', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('q_id'),
    sa.UniqueConstraint('ques')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('marks', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_marks'), 'user', ['marks'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_marks'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('questions')
    # ### end Alembic commands ###