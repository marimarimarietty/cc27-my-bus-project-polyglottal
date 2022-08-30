from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import api.schemas.notifications as notifications_schema

import api.cruds.notifications as notifi_crud
from api.db import get_db

router = APIRouter()


@router.get("/notifications", response_model=List[notifications_schema.Notifications])
async def list_notification(db: AsyncSession = Depends(get_db)):
    return await notifi_crud.get_notifications(db)


@router.post("/notifications", response_model=notifications_schema.NotifiCreateResponse)
async def create_notifications(
  notifi_body: notifications_schema.NotifiCreate, db: AsyncSession = Depends(get_db)
):
  return await notifi_crud.create_notifications(db, notifi_body)


@router.patch("/notifications/{busanduser_id}", response_model=notifications_schema.NotifiCreateResponse)
async def update_notifications(notifi_id: int, notifi_body: notifications_schema.NotifiCreate):
    return notifications_schema.NotifiCreateResponse(id=notifi_id, **notifi_body.dict())


@router.delete("/notifications/{busanduser_id}", response_model=None)
async def delete_notifications(notifi_id: int):
    return
