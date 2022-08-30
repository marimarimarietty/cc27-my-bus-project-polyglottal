from sqlalchemy.ext.asyncio import AsyncSession

import api.models.notifications as notifi_model
import api.schemas.notifications as notifi_schema

from typing import List, Tuple, Optional
from sqlalchemy import select
from sqlalchemy.engine import Result


async def create_notifications(
    db: AsyncSession, notifi_create: notifi_schema.NotifiCreate
) -> notifi_model.Notifications:
    notifi = notifi_model.Notifications(**notifi_create.dict())
    db.add(notifi)
    await db.commit()
    await db.refresh(notifi)
    return notifi

# list notifications
async def list_notifications(db: AsyncSession) -> List[Tuple[int, str]]:
    result: Result = await (
        db.execute(
            select(
                notifi_model.Notifications.id,
                notifi_model.Notifications.busroute,
                notifi_model.Notifications.direction,
                notifi_model.Notifications.busstop,
                notifi_model.Notifications.busid,
                notifi_model.Notifications.userid,
            )
        )
    )
    return result.all()

# update notification
async def get_notification(db: AsyncSession, notification_id: int) -> Optional[notifi_model.Notifications]:
    result: Result = await db.execute(
        select(notifi_model.Notifications).filter(notifi_model.Notifications.id == notification_id)
    )
    notifications: Optional[Tuple[notifi_model.Notifications]] = result.first()
    return notifications[0] if notifications is not None else None


async def update_notification(
    db: AsyncSession, notifi_create: notifi_schema.NotifiCreate, original: notifi_model.Notifications
) -> notifi_model.Notifications:
    original.done = notifi_create.done
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original
