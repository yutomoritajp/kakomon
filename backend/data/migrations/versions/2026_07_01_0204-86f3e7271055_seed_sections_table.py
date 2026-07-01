"""seed_sections_table

Revision ID: 86f3e7271055
Revises: 3a67003b2fbe
Create Date: 2026-07-01 02:04:04.976868

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '86f3e7271055'
down_revision: Union[str, Sequence[str], None] = '3a67003b2fbe'
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
