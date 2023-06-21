
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from src.db.vector_db import KnowledgeDatabase

class GPTgChatbot():
    def __init__(self, create_database = False):
        knowledge = KnowledgeDatabase()
        if create_database:
            knowledge.create_vector_db()
            knowledge.save_vector_db("data/faiss_cache/vector_db")
        else:
            knowledge.load_vector_db("data/faiss_cache/vector_db")
        self.qa = RetrievalQA.from_chain_type(llm=OpenAI(), 
                                              chain_type="stuff", 
                                              retriever=knowledge.db.as_retriever(), 
                                              return_source_documents=True)
    
    def query(self, query: str):
        result = self.qa({"query": query})
        print("Question:  ", query)
        print("Response:  ",result["result"])
        print("Source Documents:  ",result['source_documents'])
        return result