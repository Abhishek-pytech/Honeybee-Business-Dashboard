from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from database import Base
from sqlalchemy.sql import func

class ListingMaster(Base):
    __tablename__ = "listing_master"

    id = Column(Integer, primary_key=True, index=True)
    business_name = Column(String(255))
    category = Column(String(255))
    city = Column(String(255))
    address = Column(Text)
    phone = Column(String(50))
    source = Column(String(100))
    created_at = Column(TIMESTAMP, server_default=func.now())