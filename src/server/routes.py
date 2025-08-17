from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.controller.whatsapp import create_message, Message


router = APIRouter()

@router.get("/ping")
def ping():
    return JSONResponse(content={"message": "pong"}, status_code=200)

@router.post("/send")
def send(message: Message):
    return create_message(message)
    