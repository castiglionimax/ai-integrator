from pydantic import BaseModel
from fastapi.responses import JSONResponse

from app.handler.omnichannel.whatsapp import send_message
from app.model import Message as domain_message

class Message(BaseModel):
    phone: str
    text: str

def to_domain(payload: Message) -> domain_message:
    return domain_message(phone=payload.phone, text=payload.text)



def create_message(payload: Message):
   result=send_message(to_domain(payload))
   return JSONResponse(content=result, status_code=200)
