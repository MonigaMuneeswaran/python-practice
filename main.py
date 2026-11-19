
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app import chatbot
import traceback

app = FastAPI()

class ChatbotRequest(BaseModel):
    message: str
    user_id: str

class ChatbotResponse(BaseModel):
    response: str

@app.post("/my_chatbot", response_model=ChatbotResponse)
def my_chatbot(request: ChatbotRequest):
    try:
        print("Received User ID:", request.user_id)
        print("Received Message:", request.message)

        result = chatbot(request.message, request.user_id)

        print("Chatbot Response:", result)

        return ChatbotResponse(response=result)

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=f"{type(e).__name__}: {str(e)}"
        )
