from sqlalchemy.orm import Session
from sqlalchemy import func
from models import ListingMaster


def insert_listing(db: Session, listing):
    new_listing = ListingMaster(
        business_name=listing.business_name,
        category=listing.category,
        city=listing.city,
        address=listing.address,
        phone=listing.phone,
        source=listing.source
    )

    db.add(new_listing)
    db.commit()
    db.refresh(new_listing)

    return new_listing


def get_city_wise_count(db: Session):
    results = db.query(
        ListingMaster.city,
        func.count(ListingMaster.id)
    ).group_by(ListingMaster.city).all()

    return [{"city": city, "count": count} for city, count in results]


def get_category_wise_count(db: Session):
    results = db.query(
        ListingMaster.category,
        func.count(ListingMaster.id)
    ).group_by(ListingMaster.category).all()

    return [{"category": category, "count": count} for category, count in results]


def get_source_wise_count(db: Session):
    results = db.query(
        ListingMaster.source,
        func.count(ListingMaster.id)
    ).group_by(ListingMaster.source).all()

    return [{"source": source, "count": count} for source, count in results]