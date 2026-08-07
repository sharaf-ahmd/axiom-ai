"""add user role

Revision ID: b391ecb78d89
Revises: 1ac85885ba30
Create Date: 2026-08-07 05:13:07.667661

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'b391ecb78d89'
down_revision: Union[str, Sequence[str], None] = '1ac85885ba30'
branch_labels = None
depends_on = None


def upgrade() -> None:

    user_role_enum = sa.Enum(
        'USER',
        'ADMIN',
        name='userrole'
    )

    # Create PostgreSQL enum type
    user_role_enum.create(
        op.get_bind(),
        checkfirst=True
    )

    # Add column
    op.add_column(
        'users',
        sa.Column(
            'role',
            user_role_enum,
            nullable=False,
            server_default='USER'
        )
    )


def downgrade() -> None:

    op.drop_column(
        'users',
        'role'
    )

    user_role_enum = sa.Enum(
        'USER',
        'ADMIN',
        name='userrole'
    )

    user_role_enum.drop(
        op.get_bind(),
        checkfirst=True
    )