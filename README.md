# Task Flow

Multi-tenant SaaS task management system where tasks belong to an "Organization" or "Company," allowing multiple employees to view and edit the same tasks without accessing data from other companies.

## 🚀 Technologies

- Django REST Framework
- PostgreSQL
- Python 3.10

## 📋 Prerequisites

- Python 3.10 or higher

## 🔧 Installation and Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd taskflow
```

### 2. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and adjust the settings:

```bash
cp .env.example .env
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run development server

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
├── .env                 # Environment variables (not versioned)
├── .env.example         # Environment variables example
└── .gitignore          # Git ignored files
```

## 🎯 Next Steps

- [ ] Docker
- [ ] Create custom authentication app
- [ ] Create Organization/Company model
- [ ] Create Tasks model
- [ ] Implement multi-tenant system
- [ ] Create REST APIs for task CRUD
- [ ] Implement organization-based permissions
