# Quote of the Day

A simple Django web application that displays a random inspirational quote each time the homepage is visited.

This project was built to understand the complete lifecycle of a Django application—from project creation and URL routing to database interaction, template rendering, and deployment.

## Features

* Displays a random quote on every page refresh.
* Stores quotes in a SQLite database.
* Uses Django's ORM for database operations.
* Renders dynamic HTML templates.
* Clean and minimal user interface.

## Tech Stack

* Python
* Django
* SQLite
* HTML

## Project Structure

```text
quote-of-the-day/
│
├── manage.py
├── db.sqlite3
├── quote_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── pages/
│   ├── migrations/
│   ├── templates/
│   │   └── home.html
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── ...
│
└── requirements.txt
```

## How It Works

1. A user visits the homepage.
2. Django's URL dispatcher routes the request to the `home` view.
3. The view queries the database using Django's ORM.
4. A random quote is selected.
5. The quote object is passed to the template.
6. The template renders the HTML response.
7. The browser displays the quote.

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd quote-of-the-day
```

Create and activate a virtual environment:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## Learning Objectives

This project was built to understand:

* Django project structure
* URL routing
* Views
* Templates
* Models
* Migrations
* Django ORM
* Request–response lifecycle
* Database integration
* Web application deployment

## Future Improvements

* Admin interface for managing quotes
* Quote categories
* Search functionality
* Favorite quotes
* REST API
* PostgreSQL support
* Docker deployment
* User authentication

## License

This project is intended for learning and educational purposes.
