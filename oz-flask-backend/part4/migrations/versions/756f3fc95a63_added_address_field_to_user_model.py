"""added address field to user model

Revision ID: 756f3fc95a63
Revises: 
Create Date: 2024-05-02 15:47:40.601341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '756f3fc95a63'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address', sa.String(length=120), nullable=False))
        batch_op.create_unique_constraint(None, ['address'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('address')

    # ### end Alembic commands ###