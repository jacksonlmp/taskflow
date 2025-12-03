# TaskFlow - Multi-Tenant SaaS Task Management

Multi-tenant SaaS task management system where tasks belong to an "Organization" or "Company," allowing multiple employees to view and edit the same tasks without accessing data from other companies.

## 📊 Project Status

**Current Phase**: ✅ **Phase 1.5 - COMPLETE** (Multi-tenant preparation)

### Development Roadmap

#### ✅ Phase 1 - Personal Use (COMPLETE)
- [x] Django REST Framework setup with Docker
- [x] PostgreSQL database integration
- [x] Task model with CRUD API endpoints
- [x] Token-based authentication
- [x] Swagger/ReDoc API documentation
- [x] React frontend with Vite
- [x] Complete task management UI (list, create, edit, delete)
- [x] Responsive design with gradient styling

#### ✅ Phase 1.5 - Multi-Tenant Preparation (COMPLETE)
- [x] Organization model (tenant representation)
- [x] UserProfile model (user-organization relationships with roles)
- [x] Enhanced Task model with organization fields
- [x] Data migration (auto-create personal organizations)
- [x] Organization API endpoints
- [x] Enhanced Task API with organization filtering
- [x] Auto-assignment of organization on task creation
- [x] Admin panel registration for all models

**📄 Detailed Phase 1.5 documentation**: See [PHASE_1.5_COMPLETE.md](./PHASE_1.5_COMPLETE.md)

#### 🔄 Phase 2 - Full Multi-Tenant (PLANNED)
- [ ] Frontend organization selector
- [ ] Organization settings UI
- [ ] Member management interface
- [ ] Role-based permissions (UI + backend)
- [ ] Invitation system
- [ ] Multi-organization membership support
- [ ] Activity logging

## 🚀 Technologies

### Backend
- Django 5.0 REST Framework
- PostgreSQL 15 (Alpine)
- Token Authentication
- drf-spectacular (OpenAPI/Swagger)

### Frontend
- React 18
- Vite 7.2.6
- Axios for API calls

### DevOps
- Docker & Docker Compose
- Hot reload for frontend development
- Health checks for all services

## 📋 Prerequisites

### With Docker (Recommended)
- Docker
- Docker Compose

### Without Docker
- Python 3.10 or higher
- Node.js 18+ (for frontend)
- PostgreSQL 15+ (optional, can use SQLite for development)

## 🔧 Installation and Setup

### Option 1: Using Docker (Recommended)

1. **Clone the repository**
```bash
git clone <repository-url>
cd taskflow
```

2. **Build and start all services**
```bash
make build
# or
docker compose up --build
```

This will start:
- **PostgreSQL** on port 5432
- **Django Backend** on port 8000
- **React Frontend** on port 5173

3. **Run migrations** (first time only)
```bash
make migrate
```

4. **Create a superuser** (first time only)
```bash
make createsuperuser
```

5. **Access the applications**
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000/api/
- **API Docs (Swagger)**: http://localhost:8000/api/docs/
- **API Docs (ReDoc)**: http://localhost:8000/api/redoc/
- **Admin Panel**: http://localhost:8000/admin

6. **Stop containers**
```bash
make down
# or
docker compose down
```

### Option 2: Local Development (Without Docker)

#### Backend Setup

1. **Navigate to backend directory**
```bash
cd backend
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
```bash
cp .env.example .env
# Edit .env with your database settings
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Create superuser**
```bash
python manage.py createsuperuser
```

7. **Run development server**
```bash
python manage.py runserver
```

#### Frontend Setup

1. **Navigate to frontend directory** (in a new terminal)
```bash
cd frontend
```

2. **Install dependencies**
```bash
npm install
```

3. **Run development server**
```bash
npm run dev
```

## 📁 Project Structure

```
taskflow/
├── backend/                    # Django REST API
│   ├── config/                # Django settings
│   │   ├── settings.py        # Main settings
│   │   ├── urls.py            # Main routes
│   │   └── wsgi.py            # WSGI config
│   ├── tasks/                 # Tasks app
│   │   ├── models.py          # Task, Organization, UserProfile models
│   │   ├── serializers.py     # DRF serializers
│   │   ├── views.py           # ViewSets for CRUD
│   │   ├── admin.py           # Admin panel config
│   │   ├── urls.py            # App routes
│   │   └── migrations/        # Database migrations
│   ├── manage.py              # Django manager
│   ├── requirements.txt       # Python dependencies
│   ├── Dockerfile             # Backend Docker config
│   └── entrypoint.sh          # Docker entrypoint script
├── frontend/                   # React SPA
│   ├── src/
│   │   ├── components/        # React components
│   │   │   ├── Login.jsx      # Authentication
│   │   │   ├── TaskList.jsx   # Task listing with CRUD
│   │   │   └── TaskForm.jsx   # Task creation/editing modal
│   │   ├── services/
│   │   │   └── api.js         # Axios API client
│   │   ├── App.jsx            # Main app component
│   │   └── main.jsx           # React entry point
│   ├── package.json           # Node dependencies
│   ├── vite.config.js         # Vite configuration
│   └── Dockerfile             # Frontend Docker config
├── docker-compose.yml         # Multi-container orchestration
├── Makefile                   # Command shortcuts
├── README.md                  # This file
├── PHASE_1.5_COMPLETE.md     # Phase 1.5 documentation
├── .dockerignore              # Docker ignore file
├── .env.example               # Environment variables example
└── .gitignore                 # Git ignored files
```

## 🔌 API Endpoints

### Authentication
- `POST /api/auth/login/` - Login and get token
- `POST /api/auth/logout/` - Logout (invalidate token)

### Organizations
- `GET /api/organizations/` - List user's organizations
- `GET /api/organizations/{id}/` - Get organization details
- `GET /api/organizations/{id}/members/` - List organization members
- `GET /api/organizations/current/` - Get user's current organization
- `POST /api/organizations/` - Create organization
- `PUT/PATCH /api/organizations/{id}/` - Update organization
- `DELETE /api/organizations/{id}/` - Delete organization

### User Profiles
- `GET /api/profiles/` - List profiles for user's organizations
- `GET /api/profiles/{id}/` - Get profile details
- `POST /api/profiles/` - Create profile
- `PUT/PATCH /api/profiles/{id}/` - Update profile
- `DELETE /api/profiles/{id}/` - Delete profile

### Tasks
- `GET /api/tasks/` - List tasks (filtered by organization)
- `GET /api/tasks/{id}/` - Get task details
- `POST /api/tasks/` - Create task (auto-assigns organization)
- `PUT/PATCH /api/tasks/{id}/` - Update task
- `DELETE /api/tasks/{id}/` - Delete task

### API Documentation
- `GET /api/docs/` - Swagger UI
- `GET /api/redoc/` - ReDoc UI
- `GET /api/schema/` - OpenAPI Schema (JSON/YAML)

## 🐳 Docker Commands

### Using Makefile (Recommended)
```bash
make help              # Show all available commands
make build             # Build and start all containers
make up                # Start containers
make down              # Stop containers
make restart           # Restart containers
make logs              # View logs from all containers
make logs-backend      # View backend logs only
make logs-frontend     # View frontend logs only
make shell             # Access Django shell
make bash              # Access backend container bash
make migrate           # Run database migrations
make makemigrations    # Create new migrations
make createsuperuser   # Create Django superuser
make test              # Run backend tests
make collectstatic     # Collect Django static files
make clean             # Stop and remove volumes (⚠️ deletes data)
make prune             # Remove all unused Docker resources
```

### Using Docker Compose directly
```bash
docker compose up --build              # Build and start
docker compose up                      # Start containers
docker compose down                    # Stop containers
docker compose restart backend         # Restart backend only
docker compose logs -f backend         # View backend logs
docker compose exec backend python manage.py shell         # Django shell
docker compose exec backend python manage.py migrate       # Run migrations
docker compose exec backend python manage.py createsuperuser  # Create superuser
```

## 🔑 Environment Variables

Create a `.env` file in the backend directory (see `.env.example`):

```env
# Database
DB_ENGINE=django.db.backends.postgresql
DB_NAME=taskflow_db
DB_USER=taskflow_user
DB_PASSWORD=taskflow_password
DB_HOST=db
DB_PORT=5432

# Django
SECRET_KEY=your-secret-key-here
DEBUG=1
ALLOWED_HOSTS=localhost,127.0.0.1
```

## 🎨 Multi-Tenant Architecture

### Current Implementation (Phase 1.5)

**Soft Multi-Tenancy** with shared database:
- Each user gets a personal organization automatically
- Tasks belong to organizations and filter by user's organization
- Users can belong to multiple organizations (UserProfile with roles)
- Organization context auto-assigned on task creation

**Role System**:
- `owner` - Full control (can delete organization)
- `admin` - Can manage members and tasks
- `member` - Can create and edit tasks
- `viewer` - Read-only access

### Data Isolation
- ✅ Organization-level task filtering
- ✅ User can only access their organization's data
- ✅ Auto-assignment prevents data leakage
- 🔄 Phase 2: UI for org switching and role-based permissions

## 🧪 Testing

### Backend Tests
```bash
make test
# or
docker compose exec backend python manage.py test
```

### API Testing
Use the Swagger UI at http://localhost:8000/api/docs/ for interactive API testing.

Or use curl:
```bash
# Login
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"your_username","password":"your_password"}'

# Get tasks (with token)
curl -X GET http://localhost:8000/api/tasks/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

## 📝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👥 Authors

- Your Name - Initial work

## 🙏 Acknowledgments

- Django REST Framework community
- React and Vite teams
- Docker community

---

**Need help?** Check the [Phase 1.5 documentation](./PHASE_1.5_COMPLETE.md) for detailed implementation notes.
