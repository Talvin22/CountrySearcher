from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from country_searching.country_searcher import CountrySearcher
from database.database import Country

searcher = CountrySearcher()


class CashManager:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_data_from_parser(self, country_name: str):
        country_data = searcher.search_country(country_name)
        country_data_for_db = Country(country_name=country_name, country_data=country_data)
        self._session.add(country_data_for_db)
        await self._session.commit()
        return country_data_for_db

    async def get_data_from_database(self, country_name: str):
        query = select(Country).where(Country.country_name == country_name.lower().replace(" ", "-"))
        result = await self._session.execute(query)
        country = result.scalars().first()
        return country

    async def get_data(self, country_name: str):
        country = await self.get_data_from_database(country_name)
        if country:
            print("country from database")
            return country
        else:
            return await self.get_data_from_parser(country_name)
