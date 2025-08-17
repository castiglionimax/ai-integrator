import os
from twilio.rest import Client
from app.model import Message

sid = os.getenv("TWILIO_ACCOUNT_SID")
token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(sid, token)

def send_message(msg: Message):
    message = client.messages.create(
        from_="whatsapp:+18565653834", 
        to="whatsapp:+5491171659999",
        body=msg.text
    )
    
    return {
        "sid": message.sid,
        "status": message.status,
        "to": message.to,
        "body": message.body
    } 