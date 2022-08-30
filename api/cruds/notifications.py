from sqlalchemy.ext.asyncio import AsyncSession

import api.models.notifications as notifi_model
import api.schemas.notifications as notifi_schema

from typing import List, Tuple
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
async def get_notifications(db: AsyncSession) -> List[Tuple[int, str]]:
    result: Result = await (
        db.execute(
            select(
                notifi_model.Notifications.id,
                notifi_model.Notifications.busroute,
                notifi_model.Notifications.direction,
                notifi_model.Notifications.busstop,
                notifi_model.Notifications.busid,
                notifi_model.Notifications.userid,
                notifi_model.Notifications.busanduserid,
            )
        )
    )
    return result.all()
