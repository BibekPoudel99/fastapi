"""add content to post

Revision ID: ad2c4b06a9a1
Revises: 1b035eb4fffb
Create Date: 2025-12-29 13:33:12.661739

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad2c4b06a9a1'
down_revision: Union[str, Sequence[str], None] = '1b035eb4fffb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
