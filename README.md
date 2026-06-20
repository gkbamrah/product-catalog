
#  Product Catalog

A Django project to model products, tags, and categories.

 

##  How to run

Clone and enter repo:
``` 
git clone https://github.com/gkbamrah/product-catalog.git 
cd product-catalog
```
Start virtual environment:
```
python -m venv .venv 
source .venv/bin/activate # Mac/Linux 

.venv\Scripts\activate # Windows
```
Install dependencies:
```
pip install -r requirements.txt
```
Run migrations:
```
python manage.py migrate
```
Create superuser:
```
python manage.py createsuperuser
```
Run the server:
```
python manage.py runserver
```
Website will be running at ```http://127.0.0.1:8000/```

## AI Usage

AI was used in the following ways:
- Creating sample data
- Generating the HTML skeleton for the template
- Populating the gitignore file
- Making suggestions for code quality and conventions for maintainability

**No code was copied directly from AI sources. All suggestions made by AI tools were thoroughly researched and understood before including it.**

