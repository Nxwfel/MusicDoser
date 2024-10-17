"""empty message

Revision ID: d3472a2f4f45
Revises: 0e9e26cb8d11
Create Date: 2024-10-17 07:42:42.120965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3472a2f4f45'
down_revision = '0e9e26cb8d11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('is_logged')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_logged', sa.BOOLEAN(), nullable=True))

    # ### end Alembic commands ###
