# Service Store

A Django-based service management platform for tracking and managing service records.

## Features

- Service record CRUD operations
- User authentication and authorization
- Django admin panel for data management
- SQLite database for lightweight deployment
- Template-based frontend

## Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite (easily portable to PostgreSQL)
- **Frontend**: Django Templates, HTML/CSS/JavaScript

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/michealzs/serviceStore.git
cd serviceStore
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser (optional, for admin access):
```bash
python manage.py createsuperuser
```

6. Start development server:
```bash
python manage.py runserver
```

7. Access the application:
- Main app: http://localhost:8000
- Admin panel: http://localhost:8000/admin

## Project Structure

```
serviceStore/
├── main/               # Main Django app
├── settings/           # Django settings configuration
├── templates/          # HTML templates
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```

## Available Commands

```bash
# Run database migrations
python manage.py migrate

# Create database migrations
python manage.py makemigrations

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Run tests
python manage.py test
```

## License

MIT
