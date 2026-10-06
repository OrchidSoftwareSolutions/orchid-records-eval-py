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

# Runs both servers; if either exits, the other is stopped too.
dev:
	@(cd server && exec ../$(VENV)/bin/uvicorn main:app --reload --host 127.0.0.1 --port 8000) & api=$$!; \
	(cd web && exec node_modules/.bin/next dev -H 127.0.0.1 -p $(WEB_PORT)) & web=$$!; \
	trap 'kill $$api $$web 2>/dev/null; wait; exit 130' INT TERM; \
	while kill -0 $$api 2>/dev/null && kill -0 $$web 2>/dev/null; do sleep 1; done; \
	kill $$api $$web 2>/dev/null; wait; \
	echo "A server exited (see output above); stopped both."; exit 1

clean:
	rm -rf $(VENV) web/node_modules web/.next
