from src.db.vector_db import KnowledgeDatabase

def test_create_and_database():
    vector_db = KnowledgeDatabase()
    vector_db.create_vector_db()