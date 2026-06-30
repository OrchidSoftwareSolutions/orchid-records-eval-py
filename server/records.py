from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from datetime import datetime, timezone

from store import get_all_records, add_record, get_record_by_id
from auth import current_user
from logger import log

router = APIRouter()


# GET /records — list records for the current user.
@router.get("/records")
def list_records(ownerId: str | None = None):
    all_records = get_all_records()
    # Pull everything, then keep the ones for this owner.
    result = [r for r in all_records if r["ownerId"] == ownerId] if ownerId else all_records
    log("listed records", result)
    return result


# GET /records/{id} — fetch a single record.
@router.get("/records/{record_id}")
def get_record(record_id: str):
    record = get_record_by_id(record_id)
    if not record:
        return JSONResponse(status_code=404, content={"error": "not found"})
    log("fetched record", record)
    return record


# POST /records — create a record.
@router.post("/records")
async def create_record(request: Request, user_id: str = Depends(current_user)):
    body = await request.json()

    record = {
        "id": f"rec-{int(datetime.now(timezone.utc).timestamp() * 1000)}",
        "ownerId": user_id,
        "patientName": body.get("patientName"),
        "ssn": body.get("ssn"),
        "diagnosis": body.get("diagnosis"),
        "notes": body.get("notes"),
        "createdAt": datetime.now(timezone.utc).isoformat(),
    }

    add_record(record)
    log("created record", record)
    return JSONResponse(status_code=201, content=record)
