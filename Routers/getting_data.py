from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from country_searching.cash_manager import CashManager
from database.database import get_async_session

router = APIRouter(
    prefix="/country",
    tags=["country"]
)

cash_manager = CashManager()


@router.get("/{country_name}")
async def get_data(country_name: str, session: AsyncSession = Depends(get_async_session)):
    return await cash_manager.get_data(country_name, session)
