# Local setup without Docker. Everything installs into .venv/ and web/node_modules/.
.PHONY: setup dev clean

VENV := .venv
WEB_PORT ?= 3000

setup:
	@if command -v uv >/dev/null 2>&1; then \
		uv venv $(VENV) --python 3.12 && uv pip install --python $(VENV)/bin/python -r server/requirements.txt; \
	else \
		PY=$$(for p in python3.13 python3.12 python3.11 python3.10; do command -v $$p && break; done); \
		if [ -z "$$PY" ]; then echo "Need Python 3.10+ (or install uv: https://docs.astral.sh/uv/)"; exit 1; fi; \
		$$PY -m venv $(VENV) && $(VENV)/bin/pip install -r server/requirements.txt; \
	fi
	cd web && npm ci

dev:
	@trap 'kill 0' INT TERM EXIT; \
	(cd server && ../$(VENV)/bin/uvicorn main:app --reload --host 127.0.0.1 --port 8000) & \
	(cd web && npx next dev -H 127.0.0.1 -p $(WEB_PORT)) & \
	wait

clean:
	rm -rf $(VENV) web/node_modules web/.next
