import uvicorn
from fastapi import FastAPI
from src.chatbot.gptg_model import GPTgChatbot
from pydantic import BaseModel

description = """
GPTg exposes a chatbot which provides answers to the questions of transgender inividuals

##Session

You will be able to:

* **Start a new chat session** (_not implemented_).
* **End a chat session** (_not implemented_).
* **Rejoin a chat session** (_not implemented_).

##Chat

You will be able to:

* **Send a user message and recieve a response** (_not implemented_).
* **Retrieve all message from a chat session** (_not implemented_).

##Feedback

You will be able to:

* **Report a chat response as helpful, unhelpful, incorrect, or offensive** (_not implemented_).

"""

tags_metadata = [
    {
        "name": "session",
        "description": "Operations with chat sessions: starting, ending, and rejoining them.",
    },
    {
        "name": "chat",
        "description": "Sends and recieves messages between GPTg and the user",       
    },
    {
        "name": "feedback",
        "description": "Enables the user to provide feedback about the GPTg advice.",       
    },
]

class Query(BaseModel):
    message: str


gptg = GPTgChatbot()
    
gptg_app = FastAPI(title = "GPTgApp",
              description=description,
              version = "0.0.1",
              openapi_tags=tags_metadata,)

@gptg_app.get("/")
def root():
    return {"message":description}

@gptg_app.get("/session", tags = "session")
def start_new_session():
    return

@gptg_app.get("/chat", tags = "chat")
async def ask_question(query: Query):
    response = await gptg.query(query.message)
    return {"Response": response}

if __name__ == "__main__":
    uvicorn.run("src.app.api_app:gptg_app")