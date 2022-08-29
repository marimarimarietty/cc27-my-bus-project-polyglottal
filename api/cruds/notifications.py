from sqlalchemy.ext.asyncio import AsyncSession

import api.models.notifications as notifi_model
import api.schemas.notifications as notifi_schema


async def create_notifications(
    db: AsyncSession, notifi_create: notifi_schema.NotifiCreate
) -> notifi_model.Notifications:
    notifi = notifi_model.Notifications(**notifi_create.dict())
    db.add(notifi)
    await db.commit()
    await db.refresh(notifi)
    return notifi
