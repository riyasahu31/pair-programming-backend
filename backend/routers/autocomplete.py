from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/autocomplete")
def autocomplete(payload: dict):
    code = payload.get("code", "")
    suggestion = ""
    if code.strip().endswith("pri") or "print" not in code:
        suggestion = "print('Hello World')"
    return JSONResponse({"suggestion": suggestion})
