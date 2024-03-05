from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from country_searching.country_searcher import CountrySearcher
from database.database import get_async_session
from database.database import Country

router = APIRouter(
    prefix="/getting_data",
    tags=["getting_data"]
)

searcher = CountrySearcher()


@router.get("/{country_name}")
async def get_data(country_name: str, session: AsyncSession = Depends(get_async_session)):
    query = select(Country).where(Country.country_name == country_name)
    result = await session.execute(query)
    country = result.scalars().first()
    if country:
        print("country returned from database")
        return country
    else:

        country_data = searcher.search_country(country_name)
        new_country = Country(country_name=country_name, country_data=country_data)
        session.add(new_country)
        await session.commit()

        if not country_data:
            raise HTTPException(status_code=404, detail="Country not found")
        print("country returned from parsing")
        return country_data
