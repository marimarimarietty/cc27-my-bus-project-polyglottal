from typing import List
from fastapi import APIRouter
import api.schemas.notifications as notifications_schema

router = APIRouter()

@router.get("/notifications", response_model=List[notifications_schema.Notifications])
async def list_notification():
  return [notifications_schema.Notifications(id=1, busroute="odpt.Busroute:Toei.NM01", direction="3", busstop="odpt.BusstopPole:Toei.NipponKagakuMiraikan.2546.2", busid="odpt.Bus:Toei.NM01.4601.2.T280", userid="1", busanduserid="odpt.Bus:Toei.NM01.4601.2.T2801")]


@router.post("/notifications", response_model=notifications_schema.NotifiCreateResponse)
async def create_notifications(notifi_body: notifications_schema.NotifiCreate):
    return notifications_schema.NotifiCreateResponse(id=1, **notifi_body.dict())


@router.patch("/notifications/{busanduser_id}", response_model=notifications_schema.NotifiCreateResponse)
async def update_notifications(notifi_id: int, notifi_body: notifications_schema.NotifiCreate):
    return notifications_schema.NotifiCreateResponse(id=notifi_id, **notifi_body.dict())


@router.delete("/notifications/{busanduser_id}", response_model=None)
async def delete_notifications(notifi_id: int):
    return
