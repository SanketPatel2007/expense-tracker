import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="1st",
        user="postgres",
        password="Sanket",
        port="5432"
    )