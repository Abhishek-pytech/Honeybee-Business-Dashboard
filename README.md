

# Business Listings Dashboard

## Project Overview

This project is a full-stack Business Listings Dashboard built as part of the Python Development Intern assignment for Honeybee Digital.

The application collects business listing data, stores it in MySQL, provides APIs using FastAPI, and displays reports visually using a React.js dashboard.

The dashboard shows:

* City-wise business count
* Category-wise business count
* Source-wise business count

The project follows a complete data flow:

Scraper → MySQL Database → FastAPI Backend → React Dashboard

---

## Tech Stack Used

### Frontend

* React.js
* Recharts
* Axios

### Backend

* FastAPI
* SQLAlchemy
* PyMySQL

### Database

* MySQL

### Data Generation / Scraping

* Python
* Pandas
* Faker

---

## Features

### Data Collection

Generated 500+ business listings using structured sample data with realistic business names, categories, cities, addresses, phone numbers, and sources.

### Database Storage

Stored all listings inside MySQL using the `listing_master` table.

### Backend APIs

Created APIs for:

* Insert Listing API
* City-wise Count API
* Category-wise Count API
* Source-wise Count API

### Dashboard Visualization

Displayed reports using:

* Bar Chart for City-wise Count
* Pie Chart for Category-wise Count
* Pie Chart for Source-wise Count

---

## Database Table Schema

### Table Name: listing_master

Fields:

* id
* business_name
* category
* city
* address
* phone
* source
* created_at

---

## API Endpoints

### Home API

GET `/`

Returns backend status.

---

### Insert Listing API

POST `/insert-listing`

Used to insert a new business listing.

---

### City-wise Count API

GET `/city-wise-count`

Returns total businesses grouped by city.

---

### Category-wise Count API

GET `/category-wise-count`

Returns total businesses grouped by category.

---

### Source-wise Count API

GET `/source-wise-count`

Returns total businesses grouped by source.

---

## Setup Instructions

### Step 1 — Clone Repository

```bash
git clone your-github-link
```

---

### Step 2 — Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs at:

http://127.0.0.1:8000

Swagger Docs:

http://127.0.0.1:8000/docs

---

### Step 3 — Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend runs at:

http://localhost:3000

---

### Step 4 — Scraper Setup

```bash
cd scraper
python scraper.py
```

This generates:

`business_listings.csv`

---

## Challenges Faced

### CORS Error Between React and FastAPI

Resolved using FastAPI CORSMiddleware.

### SQLAlchemy JSON Response Issue

Resolved by converting SQL query tuple results into JSON dictionary format.

### Real Website Scraping Restrictions

Instead of violating scraping policies, structured realistic sample data was generated using Faker while keeping production-ready architecture.

---

## Future Improvements

* Add search and filter options
* Add pagination
* Add authentication system
* Add export reports feature
* Use live Google Maps API integration

---

## Submission Includes

* GitHub Repository
* Backend Folder
* Frontend Folder
* Scraper Folder
* Database Dump (.sql)
* Demo Video
* README.md

---

## Author

Abhishek Patel
