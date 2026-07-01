"""seed_periods_table

Revision ID: 55f9ce4a9f12
Revises: 24df08932870
Create Date: 2026-07-01 22:29:51.692302

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '55f9ce4a9f12'
down_revision: Union[str, Sequence[str], None] = '24df08932870'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


periods_table = sa.table(
    "periods",
    sa.column("name", sa.String),
    sa.column("code", sa.String),
    sa.column("sort_order", sa.Integer)
)

def upgrade() -> None:
    """Upgrade schema."""
    op.bulk_insert(
        periods_table,
        [
            {
                "name": "令和7年度",
                "code": "R7",
                "sort_order": 100
            },
            {
                "name": "令和6年度",
                "code": "R6",
                "sort_order": 101
            },
            {
                "name": "令和5年度",
                "code": "R5",
                "sort_order": 102
            },
            {
                "name": "令和4年度",
                "code": "R4",
                "sort_order": 103
            },
            {
                "name": "令和3年度",
                "code": "R3",
                "sort_order": 104
            },
            {
                "name": "令和2年度",
                "code": "R2",
                "sort_order": 105
            },
            {
                "name": "令和元年度",
                "code": "R1",
                "sort_order": 106
            },
            {
                "name": "平成30年度",
                "code": "H30",
                "sort_order": 107
            },
            {
                "name": "平成29年度",
                "code": "H29",
                "sort_order": 108
            },
            {
                "name": "平成28年度",
                "code": "H28",
                "sort_order": 109
            },
            {
                "name": "平成27年度",
                "code": "H27",
                "sort_order": 110
            },
            {
                "name": "平成26年度",
                "code": "H26",
                "sort_order": 111
            },
            {
                "name": "平成25年度",
                "code": "H25",
                "sort_order": 112
            },
            {
                "name": "平成24年度",
                "code": "H24",
                "sort_order": 113
            },
            {
                "name": "平成23年度",
                "code": "H23",
                "sort_order": 114
            },
            {
                "name": "平成22年度",
                "code": "H22",
                "sort_order": 115
            },
            {
                "name": "平成21年度",
                "code": "H21",
                "sort_order": 116
            }
        ]
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DELETE FROM periods WHERE code IN ('R7', 'R6', 'R5', 'R4', 'R3', 'R2', 'R1', 'H30', 'H29', 'H28', 'H27', 'H26', 'H25', 'H24', 'H23', 'H22', 'H21')")
