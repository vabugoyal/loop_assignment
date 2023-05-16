import datetime

from sqlalchemy import Column, String, DateTime, Integer, Time, BigInteger
from sqlalchemy.orm import relationship

from .base import BaseModel
from ..constants import CONST_STRING_LENGTH, CONST_TOKEN_LENGTH


class Store(BaseModel):
    __tablename__ = 'store'
    store_id = Column(String(CONST_STRING_LENGTH), primary_key=True, nullable=False)

class StoreStatus(BaseModel):
    __tablename__ = 'stores_status'
    store_id = Column(String(CONST_STRING_LENGTH), primary_key=True, nullable=False)
    timestamp = Column(DateTime, primary_key=True, nullable=False)
    status = Column(String(CONST_STRING_LENGTH), nullable=False)

class StoreBusinessHours(BaseModel):
    __tablename__ = 'business_hours'
    store_id = Column(String(CONST_STRING_LENGTH), primary_key=True, nullable=False)
    dayOfWeek = Column(Integer, primary_key=True, nullable=False)
    start_time_local = Column(Time)
    end_time_local = Column(Time)


class StoreTimeZone(BaseModel):
    __tablename__ = 'time_zone'
    store_id = Column(String(CONST_STRING_LENGTH), primary_key=True, nullable=False)
    time_zone = Column(String(CONST_STRING_LENGTH), nullable=False)