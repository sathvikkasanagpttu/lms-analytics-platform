# Windows Setup

PowerShell:

```powershell
cd LMS-Analytics-Platform
docker compose up --build
```

Without Docker:

```powershell
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

In another terminal:

```powershell
cd frontend
npm install
npm run dev
```
