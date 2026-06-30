# Records

Internal app for listing and managing patient **records**. Inherited from a previous team — it works, mostly. Backend is **Python (FastAPI)**, frontend is **Next.js**.

## Run it

You'll need two terminals (a Python-capable sandbox like CodeSandbox Devbox / Replit, or local).

**Backend** (http://localhost:8000)
```bash
cd server
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

**Frontend** (http://localhost:3000)
```bash
cd web
npm install
npm run dev
```

Use any tools you like, including AI. Just talk through your reasoning as you go.

---

## Ticket A — Bug report

> Support escalation: a user reported that their records list is showing records that **don't belong to them**. Some entries appear to be other people's. Please investigate and fix.

## Ticket B — Feature request

> We want users to be able to **share** one of their records with another user. Please add this.
