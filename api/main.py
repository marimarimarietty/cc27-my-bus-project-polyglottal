from fastapi import FastAPI
from api.routers import notifications

app = FastAPI()
app.include_router(notifications.router)
