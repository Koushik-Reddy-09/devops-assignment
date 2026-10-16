DevOps Assignment — Setup Instructions

>Prerequisites:
1.Docker Desktop
2.Git
3.Terraform CLI

>Run the Application Locally
1.Start Docker Desktop.
2.Open a terminal in the project root.
3.Build and start the services:
     docker compose up -d --build
4.Open the frontend at http://localhost:8080.
5.Check the backend health endpoint at http://localhost:8000/health/.

>Services
Frontend: port 8080
FastAPI backend: port 8000
Redis: port 6379
Celery worker: background task processing


>Stop the Application
docker compose down

>Terraform
The Terraform configuration is in the terraform/ directory. Initialize and validate it locally:
terraform init
terraform validate

No AWS resources are created by these commands. Cloud deployment requires AWS credentials and a separate deployment step.

>Troubleshooting

Ensure Docker Desktop is running.
Check service status with 
            docker compose ps.
View logs with 
            docker compose logs.