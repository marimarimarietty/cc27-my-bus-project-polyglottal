from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import api.schemas.users as users_schema

import api.cruds.users as user_crud
from api.db import get_db

router = APIRouter()


@router.get("/users", response_model=List[users_schema.User])
async def list_users(db: AsyncSession = Depends(get_db)):
    return await user_crud.list_users(db)


@router.post("/users", response_model=users_schema.UserCreateResponse)
async def create_user(
    user_body: users_schema.UserCreate, db: AsyncSession = Depends(get_db)
):
    return await user_crud.create_user(db, user_body)


@router.patch("/users/{user_id}", response_model=users_schema.UserCreateResponse)
async def update_user(
    user_id: int, user_body: users_schema.UserCreate, db: AsyncSession = Depends(get_db)
):
    user = await user_crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return await user_crud.update_user(db, user_body, original=user)


@router.delete("/users/{user_id}", response_model=None)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await user_crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return await user_crud.delete_user(db, original=user)
