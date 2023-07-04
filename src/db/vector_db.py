from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import DirectoryLoader, UnstructuredURLLoader
import json

class KnowledgeDatabase():
    
    def create_vector_db(self):
        file_documents = self.load_files()
        file_db = self.create_vectorstore(file_documents)
        
        url_documents = self.load_urls()
        url_db = self.create_vectorstore(url_documents)
        
        file_db.merge_from(url_db)
        self.db = file_db
        
    def load_files(self):
        file_loader = DirectoryLoader("data/sources/files/",  show_progress=True, use_multithreading=True)
        print("Loading files...")
        documents = file_loader.load()
        print(f"There are {len(documents)} file documents")
        return documents
    
    def load_urls(self):
        with open('data/sources/source_urls.json') as f:
            source_urls = json.load(f)
            
        url_list = []
        for source in source_urls["sources"]:
            url_list.extend(source["urls"])
        
        print("Loading web pages...")
        url_loader = UnstructuredURLLoader(urls=url_list)
        documents = url_loader.load()
        print(f"There are {len(documents)} url documents")
        return documents
    
    def create_vectorstore(self,documents):
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        texts = text_splitter.split_documents(documents)
        embeddings = OpenAIEmbeddings()
        return FAISS.from_documents(texts, embeddings)
        
        
    def load_vector_db(self,file_path : str):
        self.db = FAISS.load_local(file_path, embeddings=OpenAIEmbeddings())
        
    def save_vector_db(self,file_path : str):
        self.db.save_local(file_path)