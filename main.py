from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class chatbotRequest(BaseModel):
    message: str

class chatbotResponse(BaseModel):
    response: str

@app.post("/my_chatbot")
def my_chatbot(request: chatbotRequest):
    return chatbotResponse(response= "hello, I am your simple chatbot!")
                           
    return {"message": "Hello, I am your simple chatbot!"} 
