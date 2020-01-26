"""base

Revision ID: 6265c48b88a9
Revises: 
Create Date: 2020-01-26 15:06:27.548093

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6265c48b88a9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "ips",
        sa.Column("ip", sa.String, primary_key=True, unique=True),
        sa.Column("type", sa.String),
        sa.Column("continent_code", sa.String),
        sa.Column("continent_name", sa.String),
        sa.Column("country_code", sa.String),
        sa.Column("country_name", sa.String),
        sa.Column("region_code", sa.String),
        sa.Column("city", sa.String),
        sa.Column("zip", sa.String),
        sa.Column("latitude", sa.Float),
        sa.Column("longitude", sa.Float),
        sa.Column("region_name", sa.String),
        sa.Column("geoname_id", sa.String),
        sa.Column("capital", sa.String),
        sa.Column("language_code", sa.String),
        sa.Column("language_name", sa.String),
        sa.Column("language_native", sa.String),
        sa.Column("country_flag", sa.String),
        sa.Column("calling_code", sa.String),
        sa.Column("is_eu", sa.String),
    )

    op.create_table(
        "urls",
        sa.Column("url", sa.String, primary_key=True, unique=True),
        sa.Column("ip", sa.String, primary_key=True, unique=True),
        sa.Column("type", sa.String),
        sa.Column("continent_code", sa.String),
        sa.Column("continent_name", sa.String),
        sa.Column("country_code", sa.String),
        sa.Column("country_name", sa.String),
        sa.Column("region_code", sa.String),
        sa.Column("city", sa.String),
        sa.Column("zip", sa.String),
        sa.Column("latitude", sa.Float),
        sa.Column("longitude", sa.Float),
        sa.Column("region_name", sa.String),
        sa.Column("geoname_id", sa.String),
        sa.Column("capital", sa.String),
        sa.Column("language_code", sa.String),
        sa.Column("language_name", sa.String),
        sa.Column("language_native", sa.String),
        sa.Column("country_flag", sa.String),
        sa.Column("calling_code", sa.String),
        sa.Column("is_eu", sa.String),
    )


def downgrade():
    op.drop_table('ips')
    op.drop_table('urls')
