include .env


build:
	docker compose build


up:
	docker compose --env-file .env up

down:
	docker compose down 

restart:
	docker compose --env-file .env down && docker compose --env-file .env up

