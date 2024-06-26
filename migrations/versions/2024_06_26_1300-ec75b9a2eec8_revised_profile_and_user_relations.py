"""Revised profile and user relations

Revision ID: ec75b9a2eec8
Revises: b56ccb88bd22
Create Date: 2024-06-26 13:00:33.664161

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'ec75b9a2eec8'
down_revision: Union[str, None] = 'b56ccb88bd22'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profiles', sa.Column('tg_id', sa.BigInteger(), nullable=True))
    op.add_column('profiles', sa.Column('first_name', sa.String(length=100), nullable=False))
    op.add_column('profiles', sa.Column('last_name', sa.String(length=100), nullable=False))
    op.add_column('profiles', sa.Column('username', sa.String(length=30), nullable=False))
    op.add_column('profiles', sa.Column('photo_url', sa.String(length=100), nullable=False))
    op.add_column('profiles', sa.Column('date_of_birth', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.alter_column('profiles', 'about',
               existing_type=sa.VARCHAR(length=1000),
               type_=sa.String(length=2000),
               existing_nullable=False)
    op.drop_column('profiles', 'date_birth')
    op.drop_column('profiles', 'age')
    op.drop_column('profiles', 'photo')
    op.drop_column('profiles', 'name')
    op.drop_column('users', 'tg_id')
    op.drop_column('users', 'username')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.VARCHAR(length=30), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('tg_id', sa.BIGINT(), autoincrement=False, nullable=True))
    op.add_column('profiles', sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.add_column('profiles', sa.Column('photo', sa.VARCHAR(length=40), autoincrement=False, nullable=False))
    op.add_column('profiles', sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('profiles', sa.Column('date_birth', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False))
    op.alter_column('profiles', 'about',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=1000),
               existing_nullable=False)
    op.drop_column('profiles', 'date_of_birth')
    op.drop_column('profiles', 'photo_url')
    op.drop_column('profiles', 'username')
    op.drop_column('profiles', 'last_name')
    op.drop_column('profiles', 'first_name')
    op.drop_column('profiles', 'tg_id')
    # ### end Alembic commands ###
