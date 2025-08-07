import os
os.makedirs('data', exist_ok=True)

import sqlite3

def init_db():
    conn = sqlite3.connect('data/complaints.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id TEXT, 
            user TEXT, 
            category TEXT, 
            severity TEXT,
            status TEXT, 
            agent TEXT,
            email TEXT
        )
    ''')
    conn.commit()
