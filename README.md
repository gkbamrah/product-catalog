
#  remarcable-assessment

A Django project to model products, tags, and categories.

 

##  How to run

Clone and enter repo:
``` 
git clone https://github.com/gkbamrah/remarcable-assessment.git 
cd remarcable-assessment
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

## Assumptions
- Each product can belong to only one category, and can have multiple tags
- Product search is done using the product name and description

## AI Usage

AI was used in the following ways:
- Creating sample data
- Generating the HTML skeleton for the template
- Populating the gitignore file
- Making suggestions for code quality and conventions for maintainability

**No code was copied directly from AI sources. All suggestions made by AI tools were thoroughly researched and understood before including it.**
 
## Notes
- db.sqlite3 is intentionally included in this repository as it contains the required sample data (5 categories, 10 tags, 20 products) as specified in the assignment requirements.
- Product fields include description, price, and date posted for more realism.

