from sqlalchemy import Integer, Column, String, JSON, MetaData, Table


metadata = MetaData()


country = Table(
    "country",
    metadata,

    Column("id", Integer, primary_key=True),
    Column("country_name", String, nullable=False),
    Column("country_data", JSON, nullable=False)

)
