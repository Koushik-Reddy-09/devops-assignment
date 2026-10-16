                  DevOps Assignment Journey


1. Project Overview:
The project uses FastAPI for the backend, Celery for background tasks, Redis as the message broker, and an HTML frontend.

2. Tools Used:
1.Docker and Docker Compose
2.Python and FastAPI
3.Celery
4.Redis
5.Terraform
6.GitHub Actions workflow

3. Implementation Progress:

Created a Dockerfile for the backend.

Created a Dockerfile for the frontend.

Configured Docker Compose for the frontend, backend, Redis, and Celery worker.

Started all four containers locally.

Opened the frontend at http://localhost:8080.

Checked the backend health endpoint at http://localhost:8000/health/.

Created a Terraform configuration and initialized Terraform.

Validated the Terraform configuration locally.

Created a GitHub Actions CI workflow.

Added local setup instructions in instructions.md.

4. Testing:
1.Docker Compose reports the four services as running. The backend health endpoint returned a successful response during local testing.

2.Background task completion still needs to be verified in the Docker environment.

5. Remaining Work:

.Verify background task submission and completion.
.Push the project to GitHub and verify the CI workflow runs.
.Add an architecture diagram.
.Configure and deploy AWS infrastructure if required by the assignment.
.Verify cloud logging and monitoring after deployment.

6. Cost Considerations:
Local Docker testing and Terraform validation were used to avoid creating paid cloud resources. AWS deployment has not yet been completed.

7. Current Status:
Local container setup and initial infrastructure configuration are in place. Cloud deployment, live CI verification, and final end-to-end testing remain pending.