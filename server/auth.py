from fastapi import Header
from typing import Optional


# Pretend auth. In the real app this comes from a verified session token.
# For local dev we read it from a header and default to user-1.
def current_user(x_user_id: Optional[str] = Header(default=None)) -> str:
    if x_user_id:
        return x_user_id
    return "user-1"
