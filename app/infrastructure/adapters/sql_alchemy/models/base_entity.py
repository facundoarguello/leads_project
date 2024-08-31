from sqlalchemy import Column, Integer, DateTime, event
from sqlalchemy.ext.declarative import as_declarative
from datetime import datetime

@as_declarative()
class BaseEntity:
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

@event.listens_for(BaseEntity, "before_update")
def receive_before_update(mapper, connection, target):
    target.updated_at = datetime.now()