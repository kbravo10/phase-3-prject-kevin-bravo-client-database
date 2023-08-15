"""modified

Revision ID: 5d79bde352ff
Revises: a171eeb3e1df
Create Date: 2023-08-14 21:55:36.614795

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5d79bde352ff'
down_revision: Union[str, None] = 'a171eeb3e1df'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
