"""Create table user

Revision ID: 0cb2d63a753c
Revises: 
Create Date: 2024-05-02 01:20:58.113172

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0cb2d63a753c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('gender', sa.String(), nullable=False),
    sa.Column('avatar', sa.String(), nullable=True),
    sa.Column('details', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Users_id'), 'Users', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Users_id'), table_name='Users')
    op.drop_table('Users')
    # ### end Alembic commands ###
