## DevOps Assessment Assignment

### Overview

**Key components**

- **Backend** (`backend/main.py`) – FastAPI app: `POST /notify/` enqueues a Celery task, `GET /task_status/{task_id}` returns status/result.
- **Worker** (`backend/worker.py`) – Celery worker that runs the background task.
- **Redis** – Message broker and result backend for Celery.
- **Frontend** (`frontend/index.html`) – Single page that triggers a task and polls until it’s done.

**Run locally (no Docker)**

1. Start Redis.
2. From project root: `cd backend && python -m venv venv`, activate venv, `pip install -r ../requirements.txt`.
3. Terminal 1: `cd backend && celery -A worker worker --loglevel=info`.
4. Terminal 2: `cd backend && uvicorn main:app --reload --port 8000`.
5. Serve frontend: simply open index.html in browser.
---

Design and implement a workflow to:

- **Containerize the application**
  - Build Docker images for the existing backend.
  - Provide a setup to run the app locally.
  - Identify all the hardcoded values and replace those with environment variables.
  - Include any required local dependencies (e.g. message broker, database) as containers.

- **Run containers locally**
  - Provide clear commands to:
    - Build images.
    - Start the full stack.
    - View logs and debug.

- **Deploy to a cloud provider using code (no manual clicks)**
  - Use **Infrastructure as Code (IaC)** to provision all cloud resources.
  - Use **CI/CD** (GitHub Actions, GitLab CI, Azure DevOps, etc.) to build, push images, and deploy the app.

- **Maximize managed cloud services**
  - Prefer managed services over self-hosted where possible.
  - Use cloud-native logging/monitoring where reasonable (e.g. CloudWatch, Azure Monitor, Stackdriver).

- **Deliverables**
  - updated code base with IAC and build related code.
  - document your journey in `journey.md` file.
  - create `instructions.md` file for developers to run containerized setup locally.
  - simple architecture diagram to showcase cloud resources.
  - single-page frontend in `frontend/index.html` that:
    - calls the `POST /notify/` API to trigger a background task.
    - polls the `GET /task_status/{task_id}` API to show live task status and result.

## Run the Application with Docker Compose

### Prerequisites
- Docker Desktop installed and running.
- Git installed to clone the repository.

### Start the Application

Run these commands from the project root directory:
```bash
docker compose config
docker compose up --build -d
docker compose ps
```

### Access the Application
- Frontend: http://localhost:8080
- Backend API: http://localhost:8000
- API documentation: http://localhost:8000/docs

### View Logs

View logs for all services:

```bash
docker compose logs -f
```

View logs for an individual service:

```bash
docker compose logs -f backend
docker compose logs -f worker
docker compose logs -f redis
docker compose logs -f frontend
```

### Stop the Application

```bash
docker compose down
```

To stop the application and remove its containers, use the command above. It does not remove named volumes unless the `-v` option is specified.
