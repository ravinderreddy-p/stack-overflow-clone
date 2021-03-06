"""Created Comment model

Revision ID: 731cb550a6ed
Revises: 4dad83c43221
Create Date: 2021-09-25 13:54:48.857376

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '731cb550a6ed'
down_revision = '4dad83c43221'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('text', sa.String(), nullable=False))
    op.drop_column('comment', 'comment')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('comment', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('comment', 'text')
    # ### end Alembic commands ###
