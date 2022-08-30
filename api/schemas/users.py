from typing import Optional

from pydantic import BaseModel, Field

class UserBase(BaseModel):
    name: Optional[str] = Field(None, example="Marie Matsumoto")
    email: Optional[str] = Field(None, example="marie@example.com")
    password: Optional[str] = Field(None, example="1234")


class UserCreate(UserBase):
    pass


class UserCreateResponse(UserCreate):
    id: int

    class Config:
        orm_mode = True


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
