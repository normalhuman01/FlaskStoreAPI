"""empty message

Revision ID: 1da6723d89bf
Revises: 4b18a50e0c86
Create Date: 2021-03-20 18:38:48.528530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1da6723d89bf'
down_revision = '4b18a50e0c86'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users_info', sa.Column('creation_date', sa.Date(), nullable=False))
    op.drop_column('users_info', 'company')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users_info', sa.Column('company', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('users_info', 'creation_date')
    # ### end Alembic commands ###