from pydantic import BaseModel
from fastapi.responses import JSONResponse

from app.handler.omnichannel.whatsapp import send_message
from app.model import Message as domainMessage

class Message(BaseModel):
    phone: str
    text: str

def to_domain(payload: Message) -> domainMessage:
    return domainMessage(phone=payload.phone, text=payload.text)



def create_message(payload: Message):
   result=send_message(to_domain(payload))
   return JSONResponse(content=result, status_code=200)
