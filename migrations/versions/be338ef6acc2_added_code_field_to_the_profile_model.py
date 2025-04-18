"""added code field to the profile model

Revision ID: be338ef6acc2
Revises: b3f4016da056
Create Date: 2025-03-10 14:36:09.509493

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be338ef6acc2'
down_revision = 'b3f4016da056'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lab_test_profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('code', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lab_test_profiles', schema=None) as batch_op:
        batch_op.drop_column('code')

    # ### end Alembic commands ###
