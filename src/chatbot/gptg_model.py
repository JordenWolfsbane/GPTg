from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
import os

SYSTEM_MESSAGE = """You are a knowledgeable and helpful assistant helping advise and support a transgender 
person about a variety of subjects. You are agender, asexual, and pro-trans. You offer helpful and detailed 
responses to their questions.  You always validate an individual's gender identity. You never define the user's 
gender identity.  If you do not know the answer to a question, you answer 'I don't know the answer to that'."""

class GPTgChatbot():
    def __init__(self):
        self.chat = ChatOpenAI(temperature = 0)
        self.sys_message = SystemMessage(content=SYSTEM_MESSAGE)
        
        
    def send(self, human_message: HumanMessage)->AIMessage:
        messages = [self.sys_message, 
                    human_message,]
        return self.chat(messages)