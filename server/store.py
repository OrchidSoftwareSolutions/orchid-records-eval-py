# Simple in-memory data store. Resets on restart — fine for this app.

records = [
    {
        "id": "rec-1",
        "ownerId": "user-1",
        "patientName": "Alice Romero",
        "ssn": "912-44-8190",
        "diagnosis": "Hypertension",
        "notes": "Follow-up in 3 months.",
        "createdAt": "2026-01-04T10:00:00Z",
    },
    {
        "id": "rec-2",
        "ownerId": "user-1",
        "patientName": "Bruno Costa",
        "ssn": "923-19-7741",
        "diagnosis": "Type 2 Diabetes",
        "notes": "Adjust medication dosage.",
        "createdAt": "2026-01-09T14:30:00Z",
    },
    {
        "id": "rec-3",
        "ownerId": "user-2",
        "patientName": "Carla Núñez",
        "ssn": "944-02-3318",
        "diagnosis": "Asthma",
        "notes": "Prescribed inhaler. Sensitive case.",
        "createdAt": "2026-01-11T09:15:00Z",
    },
    {
        "id": "rec-4",
        "ownerId": "user-2",
        "patientName": "Diego Salas",
        "ssn": "911-55-2204",
        "diagnosis": "Migraine",
        "notes": "Referred to neurology.",
        "createdAt": "2026-01-15T16:45:00Z",
    },
]


def get_all_records():
    return records


def add_record(record):
    records.append(record)


def get_record_by_id(record_id):
    for r in records:
        if r["id"] == record_id:
            return r
    return None
