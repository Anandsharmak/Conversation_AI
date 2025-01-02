from fastapi import FastAPI, Body
from pydantic import BaseModel
from ConversationAi import chat_with_model
from QandAModel import get_answer
# FastAPI app
app = FastAPI()

# Request Body Model
class UserInput(BaseModel):
    input_type: str  # "chat" for conversation, "qa" for question-answering
    input_text: str  # The input text (either question or conversation input)
    context: str = ""  # For QA, the context is optional for conversation

# Route for conversation and Q&A
@app.post("/interact")
async def interact(data: UserInput):
    if data.input_type == "chat":
        # Handle conversation with DialogGPT
        response = chat_with_model(data.input_text, data.context)
        return {"response": response}
    elif data.input_type == "qa":
        # Handle question-answering with DistilBERT
        answer = get_answer(data.input_text, data.context)
        return {"answer": answer}
    else:
        return {"error": "Invalid input type. Use 'chat' or 'qa'."}
