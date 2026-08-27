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
                "code": "r7",
                "sort_order": 100
            },
            {
                "name": "令和6年度",
                "code": "r6",
                "sort_order": 101
            },
            {
                "name": "令和5年度",
                "code": "r5",
                "sort_order": 102
            },
            {
                "name": "令和4年度",
                "code": "r4",
                "sort_order": 103
            },
            {
                "name": "令和3年度",
                "code": "r3",
                "sort_order": 104
            },
            {
                "name": "令和2年度",
                "code": "r2",
                "sort_order": 105
            },
            {
                "name": "平成31年度",
                "code": "h31",
                "sort_order": 106
            },
            {
                "name": "平成30年度",
                "code": "h30",
                "sort_order": 107
            },
            {
                "name": "平成29年度",
                "code": "h29",
                "sort_order": 108
            },
            {
                "name": "平成28年度",
                "code": "h28",
                "sort_order": 109
            },
            {
                "name": "平成27年度",
                "code": "h27",
                "sort_order": 110
            },
            {
                "name": "平成26年度",
                "code": "h26",
                "sort_order": 111
            },
            {
                "name": "平成25年度",
                "code": "h25",
                "sort_order": 112
            },
            {
                "name": "平成24年度",
                "code": "h24",
                "sort_order": 113
            },
            {
                "name": "平成23年度",
                "code": "h23",
                "sort_order": 114
            },
            {
                "name": "平成22年度",
                "code": "h22",
                "sort_order": 115
            },
            {
                "name": "平成21年度",
                "code": "h21",
                "sort_order": 116
            }
        ]
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DELETE FrOM periods WhErE code IN ('r7', 'r6', 'r5', 'r4', 'r3', 'r2', 'r1', 'h30', 'h29', 'h28', 'h27', 'h26', 'h25', 'h24', 'h23', 'h22', 'h21')")
