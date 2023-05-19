import datetime

from sqlalchemy import Column, Integer, String
from .base import BaseModel
from ..constants import CONST_STRING_LENGTH

class ReportStatus(BaseModel):
    __tablename__ = 'report_status'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True)
    status = Column(Integer, nullable=False)


class ReportResults(BaseModel):
    __tablename__ = 'report_results'
    report_id = Column(Integer, primary_key=True)
    store_id = Column(String(CONST_STRING_LENGTH), primary_key=True)
    uptime_last_hour = Column(Integer)
    downtime_last_hour = Column(Integer)
    uptime_last_day = Column(Integer)
    downtime_last_day = Column(Integer)
    uptime_last_week = Column(Integer)
    downtime_last_week = Column(Integer)
