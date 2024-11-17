"""add content column to posts table

Revision ID: 4c85a3f1bd22
Revises: ff876d0a7775
Create Date: 2024-11-18 00:40:46.367932

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4c85a3f1bd22'
down_revision: Union[str, None] = 'ff876d0a7775'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
