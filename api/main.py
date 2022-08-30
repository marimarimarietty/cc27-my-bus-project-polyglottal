from fastapi import FastAPI
from api.routers import notifications, users

app = FastAPI()
app.include_router(notifications.router)
app.include_router(users.router)
