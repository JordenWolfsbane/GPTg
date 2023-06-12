from src.db.db_setup import ChatDatabase
import psycopg2
import pytest


def test_create_connection():
    db= ChatDatabase()
    cursor = db.cursor()
    cursor.execute("select 1;")
    resp = cursor.fetchone()
    assert resp == (1,)
    db.disconnect()
    
def test_disconnect_reconnect():
    db= ChatDatabase()
    db.disconnect()
    db.connect()
    cursor = db.cursor()
    cursor.execute("select 1;")
    resp = cursor.fetchone()
    assert resp == (1,)
    db.disconnect()
    
def test_create_sessions_table():
    db = ChatDatabase()
    db.create_sessions_table()
    cur = db.cursor()
    
    curr.execute("INSERT INTO sessions()")
    