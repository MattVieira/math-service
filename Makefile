stop:
	docker stop $$(docker ps -qa) || true

remove-container: stop
	docker rm $$(docker ps -qa) || true

build:
	docker build -t math-service .

up: remove-container build
	docker run -d --name math-service -p 8000:8000 math-service

test: up
	docker exec math-service pytest tests/*

lint: up
	docker exec math-service pylint *.py
