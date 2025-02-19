# Makefile

.PHONY: backend tests

backend:
	docker compose up -d --no-deps --build backend
	
tests:
	docker compose up --no-deps --build tests
