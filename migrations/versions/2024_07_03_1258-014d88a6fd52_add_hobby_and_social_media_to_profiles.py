"""add hobby and social media to profiles

Revision ID: 014d88a6fd52
Revises: afbe01daa6df
Create Date: 2024-07-03 12:58:10.757951

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '014d88a6fd52'
down_revision: Union[str, None] = 'afbe01daa6df'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profiles', sa.Column('hobby', postgresql.ARRAY(sa.String()), nullable=True))
    op.add_column('profiles', sa.Column('soc_media', postgresql.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('profiles', 'soc_media')
    op.drop_column('profiles', 'hobby')
    # ### end Alembic commands ###
