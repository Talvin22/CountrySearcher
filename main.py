from fastapi import FastAPI

from Routers.getting_data import router

app = FastAPI(title="City_Looker")

app.include_router(router=router)



