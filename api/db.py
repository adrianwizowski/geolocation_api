import databases
import sqlalchemy

from api.settings import DATABASE_URL

metadata = sqlalchemy.MetaData()

multiplied_columns = (
    sqlalchemy.Column("type", sqlalchemy.String),
    sqlalchemy.Column("continent_code", sqlalchemy.String),
    sqlalchemy.Column("continent_name", sqlalchemy.String),
    sqlalchemy.Column("country_code", sqlalchemy.String),
    sqlalchemy.Column("country_name", sqlalchemy.String),
    sqlalchemy.Column("region_code", sqlalchemy.String),
    sqlalchemy.Column("city", sqlalchemy.String),
    sqlalchemy.Column("zip", sqlalchemy.String),
    sqlalchemy.Column("latitude", sqlalchemy.Float),
    sqlalchemy.Column("longitude", sqlalchemy.Float),
    sqlalchemy.Column("region_name", sqlalchemy.String),
    sqlalchemy.Column("geoname_id", sqlalchemy.String),
    sqlalchemy.Column("capital", sqlalchemy.String),
    sqlalchemy.Column("language_code", sqlalchemy.String),
    sqlalchemy.Column("language_name", sqlalchemy.String),
    sqlalchemy.Column("language_native", sqlalchemy.String),
    sqlalchemy.Column("country_flag", sqlalchemy.String),
    sqlalchemy.Column("calling_code", sqlalchemy.String),
    sqlalchemy.Column("is_eu", sqlalchemy.String),
)

ips = sqlalchemy.Table(
    "ips",
    metadata,
    sqlalchemy.Column("ip", sqlalchemy.String, primary_key=True, unique=True),
    *multiplied_columns
)

urls = sqlalchemy.Table(
    "urls",
    metadata,
    sqlalchemy.Column("url", sqlalchemy.String, primary_key=True, unique=True),
    sqlalchemy.Column("ip", sqlalchemy.String, primary_key=True, unique=True),
    *multiplied_columns
)

database = databases.Database(DATABASE_URL)
