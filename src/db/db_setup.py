import psycopg2

class ChatDatabase():
    def __init__(self):
        self.database="postgres"
        self.host="localhost"
        self.user="postgres"
        self.password="postgres"
        self.port="5432"
        self.connect()
        
    def connect(self):
        self.conn = psycopg2.connect(database=self.database,
                        host=self.host,
                        user=self.user,
                        password=self.password,
                        port=self.port)
    
    def disconnect(self):
        if conn is not None:
            self.conn.close()
            
    def cursor(self):
        return self.conn.cursor()
    
    def create_sessions_table(self):
        command = """CREATE TABLE IF NOT EXISTS sessions(
                        session_id SERIAL PRIMARY KEY,
                        created_on TIMESTAMP,
                        last_message_id INTEGER)"""
        cursor = self.cursor()
        cursor.execute(command)
        return
    
    def create_messages_table(self):
        command = """CREATE TABLE IF NOT EXISTS messages(
                        message_id SERIAL PRIMARY KEY
                        session_id INT,
                        created_on TIMESTAMP,
                        prompt TEXT,
                        message_content TEXT,
                        response TEXT,
                        last_message_id INTEGER,
                        CONSTRAINT fk_session
                            FOREIGN KEY(session_id) 
	                        REFERENCES session(session_id))"""
        cursor = self.cursor()
        cursor.execute(command)
        return
    