# Product Catalog — Backend API

A Django REST API for managing products, tags, and categories, built to power a React/TypeScript frontend.

**Live API:** https://product-catalog-5fux.onrender.com  
**Frontend repo:** https://github.com/gkbamrah/product-catalog-ui

> Note: This is hosted on Render's free tier, which spins down after inactivity. The first request may take 30-60 seconds to wake the server.

## Tech Stack
Django, Django REST Framework, PostgreSQL (via Neon), Gunicorn, Whitenoise, CORS headers

## API Endpoints
- `GET /products/api/` — list products (supports `?search=` and `?category=` query params)
- `GET /categories/api/` — list categories

## How to run locally

Clone and enter repo:
git clone https://github.com/gkbamrah/product-catalog.git
cd product-catalog
Start virtual environment:
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows
Install dependencies:
pip install -r requirements.txt
Create a `.env` file with:
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=your-local-database-url
Run migrations:
python manage.py migrate
Run the server:
python manage.py runserver

## AI Usage
AI was used in the following ways:
- Creating sample data
- Populating the gitignore file
- Suggestions for code quality, deployment configuration, and production best practices

**No code was copied directly from AI sources. All suggestions made by AI tools were thoroughly researched and understood before including them.**