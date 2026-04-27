from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from database import SessionLocal, engine, Base
from schemas import ListingCreate
import crud

app = FastAPI()

# CORS Fix
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "FastAPI + MySQL APIs working successfully"}


@app.post("/insert-listing")
def create_listing(listing: ListingCreate, db: Session = Depends(get_db)):
    return crud.insert_listing(db, listing)


@app.get("/city-wise-count")
def city_count(db: Session = Depends(get_db)):
    return crud.get_city_wise_count(db)


@app.get("/category-wise-count")
def category_count(db: Session = Depends(get_db)):
    return crud.get_category_wise_count(db)


@app.get("/source-wise-count")
def source_count(db: Session = Depends(get_db)):
    return crud.get_source_wise_count(db)