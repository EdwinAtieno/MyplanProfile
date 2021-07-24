"""empty message

Revision ID: f5c328874eb8
Revises: 
Create Date: 2021-07-24 08:43:56.905246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5c328874eb8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('Profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('First_name', sa.String(length=50), nullable=True),
    sa.Column('Last_name', sa.String(length=50), nullable=True),
    sa.Column('User_Name', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('City', sa.String(length=80), nullable=True),
    sa.Column('Country', sa.String(length=80), nullable=True),
    sa.Column('Portfolio', sa.String(length=80), nullable=True),
    sa.Column('Bio', sa.String(length=500), nullable=True),
    sa.Column('Skills', sa.String(length=80), nullable=True),
    sa.ForeignKeyConstraint(['email'], ['users.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('User_Name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Profile')
    op.drop_table('users')
    # ### end Alembic commands ###
