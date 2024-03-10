from sqlalchemy.ext.asyncio import AsyncSession

from country_searching.query_handler import QueryHandler

query_handler = QueryHandler()


class CashManager:

    def __init__(self):
        self.__query_handler = query_handler

    async def get_data(self, country_name: str, session: AsyncSession):
        country = await self.__query_handler.get_data_from_database(country_name, session)
        if country:
            print("country from database")
            return country
        else:
            return await self.__query_handler.get_data_from_parser(country_name, session)
