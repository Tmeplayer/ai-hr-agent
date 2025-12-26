import sqlite3

DB_PATH = "hr_agent.db"


def get_connection():
    return sqlite3.connect(DB_PATH)
