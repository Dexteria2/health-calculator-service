Health Calculator Microservice

Project Overview

The Health Calculator Microservice is a Python-based REST API for calculating health metrics like BMI (Body Mass Index) and BMR (Basal Metabolic Rate). This service is containerized using Docker and deployed to Azure App Service with a CI/CD pipeline implemented via GitHub Actions.

Features

Endpoints

/bmi: Calculates BMI using height (meters) and weight (kg).

/bmr: Calculates BMR using height (cm), weight (kg), age, and gender.

Mathematical Equations

BMI Formula:


BMR Formula (Harris-Benedict):

For males:


For females:


Prerequisites

Python 3.9+

Docker

Git

Azure Account (for deployment)

Setup Instructions

1. Clone the Repository

git clone <repository-url>
cd health-calculator-service

2. Install Dependencies

make init

3. Run the Application Locally

make run

The service will be available at http://localhost:5000.

Testing Instructions

1. Run Unit Tests

Execute the following command to run the automated tests:

make test

2. Manual Testing with curl

Test BMI Calculation

curl -X POST http://localhost:5000/bmi \
-H "Content-Type: application/json" \
-d '{"weight": 70, "height": 1.75}'

Expected Response:

{
  "BMI": 22.86
}

Test BMR Calculation

curl -X POST http://localhost:5000/bmr \
-H "Content-Type: application/json" \
-d '{"weight": 70, "height": 175, "age": 25, "gender": "male"}'

Expected Response:

{
  "BMR": 1724.05
}

Deployment

1. Build Docker Image

make build

2. Run the Docker Container

docker run -p 5000:5000 health-calculator-app

3. CI/CD Pipeline

Push code changes to the main branch.

GitHub Actions workflow will:

Run tests.

Build and push the Docker image.

Deploy the container to Azure App Service.

Project Structure

health-calculator-service/
|├── app.py               # Flask API endpoints
|├── health_utils.py     # Utility functions for BMI and BMR calculations
|├── test.py             # Unit tests
|├── Dockerfile          # Docker configuration
|├── Makefile            # Automation commands
|├── requirements.txt    # Dependencies
|└── .github/workflows/ci-cd.yml  # CI/CD pipeline

Evaluation Criteria

Functionality: Ensure the /bmi and /bmr endpoints work correctly and return accurate results.

Containerization: Verify that the Docker image is functional and runs seamlessly.

Automation: Confirm that Makefile commands execute as expected.

CI/CD Pipeline: Ensure GitHub Actions automates testing and deployment successfully.

Documentation: Validate the clarity of code, comments, and instructions.

Below is an example of successful API calls via curl:

curl -X POST https://health-calculator-app-nico-euephjaagvd4aset.francecentral-01.azurewebsites.net/bmr -H "Content-Type: application/json" -
d '{"weight": 70, "height": 175, "age": 25, "gender": "male"}'

for BMR

curl -X POST https://health-calculator-app-nico-euephjaagvd4aset.francecentral-01.azurewebsites.net/bmi -H "Content-Type: application/json" -
d '{"weight": 70, "height": 1.75}'

for BMI

License

This project is licensed under the MIT License.

