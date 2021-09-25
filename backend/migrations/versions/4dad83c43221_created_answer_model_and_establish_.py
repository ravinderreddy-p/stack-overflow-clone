"""Created Answer model and establish relationships

Revision ID: 4dad83c43221
Revises: 76872191b521
Create Date: 2021-09-25 12:55:39.079651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4dad83c43221'
down_revision = '76872191b521'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.alter_column('question', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('question', 'body',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('question', 'tags',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('question', 'tags',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('question', 'body',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('question', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('name', name='users_name_key')
    )
    # ### end Alembic commands ###
