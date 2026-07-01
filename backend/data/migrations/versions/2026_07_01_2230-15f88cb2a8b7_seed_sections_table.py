"""seed_sections_table

Revision ID: 15f88cb2a8b7
Revises: 55f9ce4a9f12
Create Date: 2026-07-01 22:30:10.824515

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '15f88cb2a8b7'
down_revision: Union[str, Sequence[str], None] = '55f9ce4a9f12'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


sections_table = sa.table(
    "sections",
    sa.column("name", sa.String),
    sa.column("code", sa.String),
    sa.column("sort_order", sa.Integer)
)

def upgrade() -> None:
    """Upgrade schema."""
    op.bulk_insert(
        sections_table,
        [
            {
                "name": "午前Ⅰ",
                "code": "am1",
                "sort_order": 1
            },
            {
                "name": "午前Ⅱ",
                "code": "am2",
                "sort_order": 2
            },
            {
                "name": "午後Ⅰ",
                "code": "pm1",
                "sort_order": 3
            },
            {
                "name": "午後Ⅱ",
                "code": "pm2",
                "sort_order": 4
            }
        ]
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DELETE FROM sections WHERE code IN ('am1', 'am2', 'pm1', 'pm2')")