from doctest import Example
from typing import Optional

from pydantic import BaseModel, Field

class NotifiBase(BaseModel):
    busroute: Optional[str] = Field(None, example="odpt.Busroute:Toei.NM01")
    direction: Optional[str] = Field(None, example="3")
    busstop: Optional[str] = Field(None, example="odpt.BusstopPole:Toei.NipponKagakuMiraikan.2546.2")
    busid: Optional[str] = Field(None, example="odpt.Bus:Toei.NM01.4601.2.T280")
    userid: Optional[int] = Field(None, example=1)
    busanduserid: Optional[str] = Field(None, example="odpt.Bus:Toei.NM01.4601.2.T2801")

class NotifiCreate(NotifiBase):
  pass

class NotifiCreateResponse(NotifiCreate):
    id: int

    class Config:
        orm_mode = True

class Notifications(NotifiBase):
    id: int
    done: int = Field(0, description="flag")

    class Config:
      orm_mode = True

