"""Quotes

Revision ID: 6e46d6b40dbc
Revises:
Create Date: 2023-07-23 12:31:11.538443

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "6e46d6b40dbc"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "routes",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("starting_country", sa.String(length=32), nullable=False),
        sa.Column("destination_country", sa.String(length=32), nullable=False),
        sa.Column("shipping_channel", sa.String(length=10), nullable=False),
        sa.Column("min_shipping_range", sa.Integer(), nullable=False),
        sa.Column("max_shipping_range", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "rates",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("min_weight_kg", sa.Float(), nullable=False),
        sa.Column("max_weight_kg", sa.Float(), nullable=False),
        sa.Column("per_kg_rate", sa.Float(), nullable=False),
        sa.Column("route_id", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["route_id"],
            ["routes.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("rates")
    op.drop_table("routes")
    # ### end Alembic commands ###
