from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from country_searching.country_searcher import CountryParser
from database.database import Country

searcher = CountryParser()


class QueryHandler:
    def __init__(self):
        self.__searcher = searcher

    async def get_data_from_parser(self, country_name: str, session: AsyncSession):
        country_data = self.__searcher.search_country(country_name)
        country_data_for_db = Country(country_name=country_name, country_data=country_data)
        session.add(country_data_for_db)
        await session.commit()
        return country_data_for_db

    async def get_data_from_database(self, country_name: str, session: AsyncSession):
        query = select(Country).where(Country.country_name == country_name.lower().replace(" ", "-"))
        result = await session.execute(query)
        country = result.scalars().first()
        return country
