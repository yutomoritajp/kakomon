"""seed_exams_table

Revision ID: 7723d4018663
Revises: 27326435b78d
Create Date: 2026-08-27 12:49:09.097602

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = "7723d4018663"
down_revision: Union[str, Sequence[str], None] = "27326435b78d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute(
        "INSERT INTO exams (period_code, section_code) "
        "SELECT p.code, s.code FROM periods p CROSS JOIN sections s"
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DELETE FROM exams")
