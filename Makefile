# Makefile for Health Calculator Service

init:
	@echo "Initialization: Creating virtual environment and installing dependencies...";
	python3 -m venv .venv; \
	. .venv/bin/activate && \
	pip install -r requirements.txt

run:
	@echo "Running Flask app...";
	. .venv/bin/activate && \
	python app.py

build:
	@echo "Building Docker image...";
	docker build -t health-calculator-service .

run-container:
	@echo "Running Docker container...";
	docker run -p 5000:5000 health-calculator-service

test:
	@echo "Running unit tests...";
	. .venv/bin/activate && \
	python test.py

test-api:
	@echo "Testing API endpoints...";
	curl -X POST http://127.0.0.1:5000/bmi -H "Content-Type: application/json" -d '{"height": 1.75, "weight": 70}'

stop:
	@echo "Stopping running containers...";
	docker ps -q | xargs -r docker stop

clean:
	@echo "Cleaning up Docker containers...";
	docker ps -a -q | xargs -r docker rm

help:
	@echo "Available commands:";
	@echo "  make init          - Initialize virtual environment and install dependencies";
	@echo "  make run           - Run the Flask app";
	@echo "  make build         - Build the Docker image";
	@echo "  make run-container - Run the app in a Docker container";
	@echo "  make test          - Run unit tests";
	@echo "  make test-api      - Run API endpoint tests";
	@echo "  make stop          - Stop running containers";
	@echo "  make clean         - Remove stopped containers";
