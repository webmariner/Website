"""empty message

Revision ID: 95c452965b74
Revises: 4b1bbd4c38af
Create Date: 2024-05-18 01:40:10.873575

"""

# revision identifiers, used by Alembic.
revision = '95c452965b74'
down_revision = '4b1bbd4c38af'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('arrivals_view_version', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True,
               autoincrement=False)
    op.alter_column('arrivals_view_version', 'required_permission_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('arrivals_view_version', 'required_permission_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=False)
    op.alter_column('arrivals_view_version', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False,
               autoincrement=False)
    # ### end Alembic commands ###
