from fastapi import FastAPI
from pydantic import BaseModel

from Learning import chatbot


app = FastAPI()
class chatbotRequest(BaseModel):
    message: str

class chatbotResponse(BaseModel):
    response: str

@app.post("/my_chatbot")
def my_chatbot(request: chatbotRequest):
    response = chatbot(request.message)
    return chatbotResponse(response= response)
                        
