"""DB creation

Revision ID: 2e707cb7d116
Revises: 
Create Date: 2023-12-08 23:00:36.605115

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2e707cb7d116'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('is_subscribed', sa.Boolean(), nullable=False),
    sa.Column('referral_code', sa.String(), nullable=True),
    sa.Column('referral_code_used_count', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('referral_code')
    )
    op.create_table('referral',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('referral_claimer_id', sa.Integer(), nullable=True),
    sa.Column('referral_owner_id', sa.Integer(), nullable=True),
    sa.Column('referral_code', sa.String(), nullable=True),
    sa.Column('used', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('referral')
    op.drop_table('user')
    # ### end Alembic commands ###
