"""rewrite user db to use on site

Revision ID: 01270f6f472e
Revises: b7396d04f801
Create Date: 2024-07-01 16:50:12.125311

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '01270f6f472e'
down_revision: Union[str, None] = 'b7396d04f801'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('first_name', sa.String(length=40), nullable=False))
    op.add_column('users', sa.Column('last_name', sa.String(length=40), nullable=False))
    op.add_column('users', sa.Column('username', sa.String(length=60), nullable=False))
    op.add_column('users', sa.Column('photo_url', sa.String(length=200), nullable=False))
    op.add_column('users', sa.Column('auth_date', sa.DateTime(timezone=True), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'auth_date')
    op.drop_column('users', 'photo_url')
    op.drop_column('users', 'username')
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    # ### end Alembic commands ###