"""add description to territories

Revision ID: d586bb65f3b3
Revises: b082b8eaffe0
Create Date: 2026-06-11
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = 'd586bb65f3b3'
down_revision: Union[str, None] = 'b082b8eaffe0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("territories", sa.Column("description", sa.String(500), nullable=True))


def downgrade() -> None:
    op.drop_column("territories", "description")