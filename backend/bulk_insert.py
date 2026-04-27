import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://root:Abhi@localhost/business_dashboard"

engine = create_engine(DATABASE_URL)

df = pd.read_csv("../scraper/business_listings.csv")

df.to_sql(
    name="listing_master",
    con=engine,
    if_exists="append",
    index=False
)

print("500 listings inserted into MySQL successfully!")