from pydantic import BaseModel

class ListingCreate(BaseModel):
    business_name: str
    category: str
    city: str
    address: str
    phone: str
    source: str