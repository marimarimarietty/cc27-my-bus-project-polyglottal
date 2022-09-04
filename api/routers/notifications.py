from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import api.schemas.notifications as notifications_schema

import api.cruds.notifications as notifi_crud
from api.db import get_db

router = APIRouter()


@router.get("/notifications", response_model=List[notifications_schema.Notifications])
async def list_notifications(db: AsyncSession = Depends(get_db)):
    return await notifi_crud.list_notifications(db)


@router.post("/notifications", response_model=notifications_schema.NotifiCreateResponse)
async def create_notification(
    notifi_body: notifications_schema.NotifiCreate, db: AsyncSession = Depends(get_db)
):
    return await notifi_crud.create_notification(db, notifi_body)


@router.patch("/notifications/{notification_id}", response_model=notifications_schema.NotifiCreateResponse)
async def update_notification(
    notification_id: int, notifi_body: notifications_schema.NotifiCreate, db: AsyncSession = Depends(get_db)
):
    notification = await notifi_crud.get_notification(db, notification_id=notification_id)
    if notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")

    return await notifi_crud.update_notification(db, notifi_body, original=notification)


@router.delete("/notifications/{notification_id}", response_model=None)
async def delete_notification(notification_id: int, db: AsyncSession = Depends(get_db)):
    notification = await notifi_crud.get_notification(db, notification_id=notification_id)
    if notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")

    return await notifi_crud.delete_notification(db, original=notification)
