# Task Flow

Multi-tenant SaaS task management system where tasks belong to an "Organization" or "Company," allowing multiple employees to view and edit the same tasks without accessing data from other companies.

## 🚀 Technologies

- Django REST Framework
- PostgreSQL
- Docker
- Python 3.10+

## 📋 Prerequisites

### With Docker (Recommended)
- Docker
- Docker Compose

### Without Docker
- Python 3.10 or higher
- PostgreSQL (optional, can use SQLite for development)

## 🔧 Installation and Setup

### Option 1: Using Docker (Recommended)

1. **Clone the repository**
```bash
git clone <repository-url>
cd taskflow
```

2. **Build and start containers**
```bash
make build
# or
docker compose up --build
```

3. **Create a superuser** (in a new terminal)
```bash
make createsuperuser
# or
docker compose exec web python manage.py createsuperuser
```

4. **Access the application**
- API: http://localhost:8000
- Admin: http://localhost:8000/admin

5. **Stop containers**
```bash
make down
# or
docker compose down
```

### Option 2: Local Development (Without Docker)

1. **Clone the repository**
```bash
git clone <repository-url>
cd taskflow
```

2. **Create and activate virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

For local development with SQLite, comment out or remove the `DB_ENGINE` line in `.env`.

For PostgreSQL, ensure the database connection settings are correct.

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Create a superuser**
```bash
python manage.py createsuperuser
```

7. **Run development server**
```bash
python manage.py runserver
```

Access: http://localhost:8000/admin

## 📁 Project Structure

```
taskflow/
├── config/              # Django settings
│   ├── settings.py      # Main settings
│   ├── urls.py          # Main routes
│   └── wsgi.py          # WSGI config
├── manage.py            # Django manager
├── requirements.txt     # Dependencies
├── Dockerfile           # Docker configuration
├── docker compose.yml   # Docker Compose configuration
├── entrypoint.sh        # Docker entrypoint script
├── Makefile             # Common commands shortcuts
├── .dockerignore        # Docker ignore file
├── .env                 # Environment variables (not versioned)
├── .env.example         # Environment variables example
└── .gitignore          # Git ignored files
```

## 🐳 Docker Commands

### Using Makefile (Recommended)
```bash
make help              # Show all available commands
make build             # Build and start containers
make up                # Start containers
make down              # Stop containers
make restart           # Restart containers
make logs              # View logs
make shell             # Access Django shell
make bash              # Access container bash
make migrate           # Run migrations
make makemigrations    # Create new migrations
make createsuperuser   # Create superuser
make test              # Run tests
make collectstatic     # Collect static files
make clean             # Stop and remove volumes
make prune             # Remove all unused Docker resources
```

### Using Docker Compose directly
```bash
docker compose up --build              # Build and start
docker compose up                      # Start containers
docker compose down                    # Stop containers
docker compose logs -f                 # View logs
docker compose exec web python manage.py shell         # Django shell
docker compose exec web python manage.py migrate       # Run migrations
docker compose exec web python manage.py createsuperuser  # Create superuser
docker compose exec web python manage.py collectstatic    # Collect static
```

## 🎯 Next Steps

- [x] Docker setup
- [ ] Create custom authentication app
- [ ] Create Organization/Company model
- [ ] Create Tasks model
- [ ] Implement multi-tenant system
- [ ] Create REST APIs for task CRUD
- [ ] Implement organization-based permissions
