Python 3.13.5

Student Task: Filter and Paginate Your API + Create a Custom Command
Use an existing DRF API (or create a simple model like Product with name, category, price).

Add Pagination

Use PageNumberPagination or LimitOffsetPagination in settings.py.
Create custom pagination class
Ensure /products/ returns paginated results.
Add Filtering

Use django-filter to allow filtering by fields like category or price range (price__gte, price__lte).
Example: /products/?category=Books&price__lte=100
Create a Custom Django Management Command

Create a command like python manage.py count_products that prints the number of products in the database.
