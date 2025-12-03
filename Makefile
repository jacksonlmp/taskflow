.PHONY: help up down build restart logs shell migrate makemigrations createsuperuser test collectstatic clean prune

help:
	@echo "TaskFlow - Makefile Commands"
	@echo "=============================="
	@echo "make up              - Start containers"
	@echo "make build           - Build and start containers"
	@echo "make down            - Stop containers"
	@echo "make restart         - Restart containers"
	@echo "make logs            - View logs"
	@echo "make logs-backend    - View backend logs"
	@echo "make logs-frontend   - View frontend logs"
	@echo "make shell           - Access Django shell"
	@echo "make bash            - Access backend container bash"
	@echo "make migrate         - Run database migrations"
	@echo "make makemigrations  - Create new migrations"
	@echo "make createsuperuser - Create Django superuser"
	@echo "make test            - Run tests"
	@echo "make collectstatic   - Collect static files"
	@echo "make clean           - Stop containers and remove volumes"
	@echo "make prune           - Remove all unused Docker resources"

up:
	docker compose up

build:
	docker compose up --build

down:
	docker compose down

restart:
	docker compose restart

logs:
	docker compose logs -f

logs-backend:
	docker compose logs -f backend

logs-frontend:
	docker compose logs -f frontend

shell:
	docker compose exec backend python manage.py shell

bash:
	docker compose exec backend bash

migrate:
	docker compose exec backend python manage.py migrate

makemigrations:
	docker compose exec backend python manage.py makemigrations

createsuperuser:
	docker compose exec backend python manage.py createsuperuser

test:
	docker compose exec backend python manage.py test

collectstatic:
	docker compose exec backend python manage.py collectstatic --noinput

clean:
	docker compose down -v

prune:
	docker system prune -af --volumes
