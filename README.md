# LMS Analytics Platform

Professional end-to-end Learning Management System (LMS) analytics reference implementation.

## What this project demonstrates

- React + Vite analytics portal
- FastAPI backend with REST endpoints
- PostgreSQL-ready OLTP model
- Star-schema analytical warehouse
- Bronze/Silver/Gold ELT structure
- dbt models for dimensional analytics
- Airflow orchestration example
- Event telemetry examples
- KPI calculations: DAU/MAU, completion, watch completion, quiz pass rate, revenue
- Instructor/admin dashboard UI
- Docker Compose local development
- Seed/demo data
- API documentation and architecture documentation

## Architecture

React dashboard -> FastAPI -> PostgreSQL/warehouse APIs
Learning events -> raw/bronze -> silver -> gold star schema -> BI

## Quick start

### 1. Start services

```bash
docker compose up --build
```

Frontend: http://localhost:5173
API: http://localhost:8000
API docs: http://localhost:8000/docs
PostgreSQL: localhost:5432

### 2. Local frontend without Docker

```bash
cd frontend
npm install
npm run dev
```

### 3. Local backend without Docker

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Windows PowerShell activation:
```powershell
.venv\Scripts\Activate.ps1
```

## Demo credentials

The demo dashboard does not require authentication. The API includes a simple health endpoint and demo analytics endpoints.

## Production evolution

Replace the demo in-memory analytics repository with PostgreSQL + dbt-generated Gold tables, connect Kafka/RudderStack/Segment for telemetry, and connect Superset/Power BI to the Gold layer.

## Project structure

- `frontend/` - React analytics portal
- `backend/` - FastAPI API
- `warehouse/` - dbt-style star schema models
- `airflow/` - orchestration DAG
- `data/` - demo telemetry/OLTP seed data
- `docs/` - architecture, data dictionary and interview notes
- `superset/` - BI dashboard configuration notes
- `docker-compose.yml` - local infrastructure

## Portfolio value

This project is designed to demonstrate Data Analyst / BI / Analytics Engineering skills:
SQL, dimensional modeling, KPI design, ELT, data quality, Python, APIs, dashboard design, and modern data architecture.
