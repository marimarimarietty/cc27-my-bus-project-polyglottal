from sqlalchemy.ext.asyncio import AsyncSession

import api.models.notifications as user_model
import api.schemas.users as user_schema

from typing import List, Tuple, Optional
from sqlalchemy import select
from sqlalchemy.engine import Result


async def create_user(
    db: AsyncSession, user_create: user_schema.UserCreate
) -> user_model.User:
    user = user_model.User(**user_create.dict())
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

#  list users
async def list_users(db: AsyncSession) -> List[Tuple[int, str]]:
    result: Result = await (
        db.execute(
            select(
                user_model.User.id,
                user_model.User.name,
                user_model.User.email,
            )
        )
    )
    return result.all()
