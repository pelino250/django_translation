# Django Translation - Class Demo

## Description

A small Django project highlighting how to set Internationalization & Localization. It also includes some examples of Caching using both Django's built-in Caching mechanism and Redis.

## Installation

### Prerequisites
- Python 3.9 and above
- pip
- Docker

### Installing

1. Clone the repository
```bash
git clone https://github.com/pelino250/django_translation.git
```

2. Navigate to the project directory
```bash
cd project
```
3. Install the required Python packages
```bash
pip install -r requirements.txt
```
4. Copy the `.env.example` file and rename it to `.env`. Update the `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, and `DJANGO_ALLOWED_HOSTS` variables in the `.env` file with your own values.

5. Run the Django migrations
```bash
python manage.py migrate
```

6. Start the Docker services
```bash
docker-compose up -d
```
6. Run the Django server
```bash
python manage.py runserver
```

