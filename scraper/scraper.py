from faker import Faker
import pandas as pd
import random

fake = Faker()

categories = [
    "Gym", "Hospital", "Restaurant",
    "Salon", "Coaching Center", "School"
]

cities = [
    "Delhi", "Mumbai", "Varanasi",
    "Lucknow", "Pune", "Noida"
]

sources = [
    "Justdial", "Google Maps", "Sulekha"
]

data = []

for i in range(500):
    listing = {
        "business_name": fake.company(),
        "category": random.choice(categories),
        "city": random.choice(cities),
        "address": fake.address(),
        "phone": fake.phone_number(),
        "source": random.choice(sources)
    }

    data.append(listing)

df = pd.DataFrame(data)

df.to_csv("business_listings.csv", index=False)

print("500 business listings created successfully!")