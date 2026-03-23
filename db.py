from dotenv import load_dotenv
import os
import psycopg2

load_dotenv(dotenv_path=".env")
print("PASS:", os.getenv("DB_PASS"))  # debug

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        port=os.getenv("DB_PORT")
    )

def get_connection():
    return psycopg2.connect(os.getenv("DATABASE_URL"))