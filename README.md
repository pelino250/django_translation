# Project Title

## Description

Provide a brief description of what your project does. Explain the problem it solves and how it does so. Mention the technologies used (in this case, Python, Django, etc.).

## Installation

### Prerequisites

List what software and tools a user needs to have installed before they can run your project. For example:

- Python 3.x
- pip
- Docker

### Installing

1. Clone the repository
```bash
git clone https://github.com/username/project.git
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

5. Start the Docker services
```bash
docker-compose up -d
```
6. Run the Django server
```bash
python manage.py runserver
```

