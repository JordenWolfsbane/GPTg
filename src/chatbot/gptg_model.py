
from langchain.llms import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from src.db.vector_db import KnowledgeDatabase
from langchain.memory import ConversationBufferMemory
class GPTgChatbot():
    def __init__(self, create_database = False):
        knowledge = KnowledgeDatabase()
        if create_database:
            knowledge.create_vector_db()
            knowledge.save_vector_db("data/faiss_cache/vector_db")
        else:
            knowledge.load_vector_db("data/faiss_cache/vector_db")
        
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        self.qa = ConversationalRetrievalChain.from_llm(llm=ChatOpenAI(temperature=0, model="gpt-4"), 
                                              retriever=knowledge.db.as_retriever(), 
                                              return_source_documents=True,
                                              condense_question_llm = ChatOpenAI(temperature=0, model='gpt-3.5-turbo'),
                                              memory=self.memory)
    
    def query(self, query: str):
        result = self.qa({"query": query})
        print("Question:  ", query)
        print("Response:  ",result["result"])
        print("Source Documents:  ",result['source_documents'])
        return result