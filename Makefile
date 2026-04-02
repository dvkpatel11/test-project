.PHONY: up down logs test build migrate clean

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

test:
	docker-compose exec backend pytest

build:
	docker-compose exec frontend npm run build

migrate:
	docker-compose exec backend alembic upgrade head

clean:
	docker-compose down -v --rmi all --remove-orphans
	rm -rf node_modules
