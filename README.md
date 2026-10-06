# Records

Internal app for listing and managing patient **records**. Inherited from a previous team — it works, mostly. Backend is **Python (FastAPI)**, frontend is **Next.js**.

## Run it

Pick whichever is easiest. All three give you the app at **http://localhost:3000** (the backend runs on :8000 and is proxied through the frontend at `/api`).

### Option 1: GitHub Codespaces (nothing to install)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/OrchidSoftwareSolutions/orchid-records-eval-py?quickstart=1)

Click the button and sign in with your GitHub account. Codespaces' free monthly allowance covers this exercise. Dependencies install and both servers start automatically; the app opens in a new tab. If you need to restart the servers, run `make dev` in the terminal.

### Option 2: Docker (local, isolated)

Requires [Docker Desktop](https://www.docker.com/products/docker-desktop/) or another Docker engine.

```bash
docker compose up
```

Everything runs in containers and is reachable only from your machine. Edits to files reload automatically. Stop with `Ctrl-C`, clean up with `docker compose down`.

### Option 3: Local, no Docker

Requires Node 20+ and either [uv](https://docs.astral.sh/uv/) or Python 3.10+.

```bash
make setup   # installs into .venv/ and web/node_modules/ only
make dev     # starts both servers; Ctrl-C stops both
```

Port 3000 taken? Use `make dev WEB_PORT=3001` (or `WEB_PORT=3001 docker compose up`).

Use any tools you like, including AI. Just talk through your reasoning as you go.

---

## Ticket A — Bug report

> Support escalation: a user reported that their records list is showing records that **don't belong to them**. Some entries appear to be other people's. Please investigate and fix.

## Ticket B — Feature request

> We want users to be able to **share** one of their records with another user. Please add this.
