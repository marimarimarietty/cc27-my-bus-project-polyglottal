from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base


class Notifications(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True)
    busroute = Column(String(1024))
    direction = Column(String(10))
    busstop = Column(String(1024))
    busid = Column(String(1024))
    userid = Column(Integer, ForeignKey("users.id"))
    busanduserid = Column(String(1024))
    done = Column(Integer)

    user = relationship("User", back_populates="notifications")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(1024))
    email = Column(String(1024))
    password = Column(String(1024))

    notifications = relationship("Notifications", back_populates="user")
