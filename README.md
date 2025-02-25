# Django Translation - Class Demo

## Description

A small Django project highlighting how to set Internationalization & Localization. It also includes some examples of Caching using both Django's built-in Caching mechanism and Redis.

## Features

- Multi-language support (English, French, and Spanish)
- Redis-based caching system
- Language switching functionality
- Translation management
- Example of translated content
- Docker integration for Redis

## Installation

### Prerequisites
- Python 3.9 and above
- pip
- Docker and Docker Compose

### Installing

1. Clone the repository
```bash
git clone https://github.com/pelino250/django_translation.git
```

2. Navigate to the project directory
```bash
cd django_translation
```

3. Install the required Python packages
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Copy the `.env.example` file and rename it to `.env`
   - Update the following variables in the `.env` file:
     ```
     DJANGO_SECRET_KEY=your-secret-key-here
     DJANGO_DEBUG=True  # Set to False in production
     DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
     REDIS_HOST=localhost
     REDIS_PORT=6379
     REDIS_DB=1
     ```

5. Start the Docker services (Redis)
```bash
docker-compose up -d
```

6. Run the Django migrations
```bash
python manage.py migrate
```

7. Compile translation messages
```bash
python manage.py compilemessages
```

8. Run the Django development server
```bash
python manage.py runserver
```

## Usage

### Language Switching
- The application supports English (default), French, and Spanish
- Use the language selector in the navigation bar to switch between languages
- URLs include language prefix (e.g., /en/, /fr/, /es/)

### Translation Management
To add or update translations:

1. Extract messages for translation:
```bash
python manage.py makemessages -l fr  # For French
python manage.py makemessages -l es  # For Spanish
```

2. Edit the translation files in the `locale/<language>/LC_MESSAGES/django.po` files

3. Compile the messages:
```bash
python manage.py compilemessages
```

### Caching
The project uses Redis for caching:
- Default cache timeout: 300 seconds
- Cache prefix: 'django_translation'
- Redis connection settings can be configured in the `.env` file

## Development

### Adding New Languages
1. Add the language code to LANGUAGES in settings.py
2. Create message files:
```bash
python manage.py makemessages -l <language_code>
```
3. Add translations to the new .po file
4. Compile messages

### Environment Variables
All configuration is done through environment variables:
- `DJANGO_SECRET_KEY`: Django secret key
- `DJANGO_DEBUG`: Debug mode (True/False)
- `DJANGO_ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `REDIS_HOST`: Redis host (default: localhost)
- `REDIS_PORT`: Redis port (default: 6379)
- `REDIS_DB`: Redis database number (default: 1)

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
