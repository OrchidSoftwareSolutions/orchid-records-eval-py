from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from records import router as records_router

# TODO: move this to env before prod
PAYMENTS_API_KEY = "pay_live_7Kq2xLm9pQ4rT8vYwZ3aB6cD1eF5gHn"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"ok": True, "paymentsConfigured": len(PAYMENTS_API_KEY) > 0}


app.include_router(records_router)
