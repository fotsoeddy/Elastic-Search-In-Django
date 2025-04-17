
# Elastic Search in Django

This is a Django web application that implements a real-time search feature using Elasticsearch. The application allows users to search for products, suppliers, brands, and categories in a database, with results displayed dynamically without page reloads. The search is triggered on keypress, features smooth animations, and uses Tailwind CSS for styling.

## Features

- **Real-Time Search**: Search across multiple models (Product, Supplier, Brand, Category) as you type, with debounced keypress events.
- **No Page Reload**: Uses AJAX to fetch and display search results in JSON format.
- **Smooth Animations**: Results fade in and slide in with staggered animations using Tailwind CSS.
- **Fixed Search Bar**: The search input remains sticky at the top of the page.
- **Responsive Design**: Styled with Tailwind CSS for a modern, responsive UI.
- **Elasticsearch Integration**: Leverages django-elasticsearch-dsl for efficient full-text search.
- **Class-Based View**: The search endpoint uses a Django class-based view (SearchJsonView) for modularity.

## Prerequisites

- Python 3.8+
- Elasticsearch 8.x
- Django 3.2+
- Node.js (optional, for Tailwind CSS if customizing)
- Git

## Setup Instructions

### Clone the Repository:
```
git clone https://github.com/fotsoeddy/Elastic-Search-In-Django.git
cd Elastic-Search-In-Django
```

### Create and Activate a Virtual Environment:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies:
```
pip install django django-elasticsearch-dsl elasticsearch
```

### Install and Start Elasticsearch:

- Download and install Elasticsearch 8.x from elastic.co.
- Start Elasticsearch: `elasticsearch`
- Verify it’s running:
  ```
  curl http://localhost:9200
  ```

### Apply Database Migrations:
```
python manage.py makemigrations
python manage.py migrate
```

### Create and Populate Elasticsearch Indices:
```
python manage.py search_index --create
python manage.py search_index --rebuild
```

### Add Sample Data (Optional): Run the following in a Python shell to add test data:
```
python manage.py shell
from store.models import Category, Brand, Supplier, Product
category = Category.objects.create(name="Electronics")
brand = Brand.objects.create(name="TechBrand")
supplier = Supplier.objects.create(name="TechSupplier", email="tech@supplier.com", phone="1234567890")
Product.objects.create(
    name="Laptop",
    category=category,
    brand=brand,
    supplier=supplier,
    description="A high-performance laptop",
    price=999.99,
    stock=10
)
```

Rebuild indices after adding data:
```
python manage.py search_index --rebuild
```

### Run the Development Server:
```
python manage.py runserver
```
Open your browser and navigate to http://localhost:8000.

## Usage

- **Search Interface**: Enter a query in the search bar at the top of the page. Results for products, suppliers, brands, and categories appear dynamically below the search bar as you type.
- **No Page Reload**: The page does not refresh; results are fetched via AJAX from the `/search` endpoint.
- **Animations**: Results fade in, and individual items slide in with a staggered effect.
- **Responsive UI**: The interface is styled with Tailwind CSS and works on various screen sizes.

## Project Structure

```
Elastic-Search-In-Django/
├── project/
│   ├── settings.py         # Django settings with Elasticsearch configuration
│   ├── urls.py            # Project-level URL routing
│   └── wsgi.py
├── store/
│   ├── models.py          # Django models (Product, Supplier, Brand, Category, etc.)
│   ├── views.py           # Class-based view for JSON search and index view
│   ├── documents.py       # Elasticsearch document mappings
│   ├── urls.py            # App-level URL routing
│   └── templates/store/
│       └── index.html     # Search interface with AJAX and Tailwind CSS
├── .gitignore             # Git ignore file for Python/Django/Elasticsearch
├── manage.py
└── README.md
```

## Debugging

- **AJAX Issues**: Check the browser’s Network tab for `/search?q=<query>` requests. Ensure JSON responses are correct.
- **Elasticsearch**: Verify data is indexed: `curl -X GET "http://localhost:9200/products/_search?pretty"`
- **JavaScript Errors**: Use the browser’s Console tab to debug AJAX or animation issues.
- **Search Results**: Test the JSON endpoint directly: http://localhost:8000/search?q=laptop.

## Contributing

- Fork the repository.
- Create a new branch (`git checkout -b feature/your-feature`).
- Commit your changes (`git commit -m "Add your feature"`).
- Push to the branch (`git push origin feature/your-feature`).
- Open a Pull Request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or issues, contact fotsoeddy or open an issue on this repository.
