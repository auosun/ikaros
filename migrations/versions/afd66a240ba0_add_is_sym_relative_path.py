"""add is_sym_relative_path

Revision ID: afd66a240ba0
Revises: ae24eb9602af
Create Date: 2024-12-31 23:29:47.864965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afd66a240ba0'
down_revision = 'ae24eb9602af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('scrapingconfigs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_sym_relative_path', sa.Boolean(), nullable=True))

    with op.batch_alter_table('transferconfigs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_sym_relative_path', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transferconfigs', schema=None) as batch_op:
        batch_op.drop_column('is_sym_relative_path')

    with op.batch_alter_table('scrapingconfigs', schema=None) as batch_op:
        batch_op.drop_column('is_sym_relative_path')

    # ### end Alembic commands ###
