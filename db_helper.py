import pyodbc
from config import Config

def get_db_connection():
    connection_string = (
        f"DRIVER={Config.AZURE_SQL_DRIVER};"
        f"SERVER={Config.AZURE_SQL_SERVER};"
        f"DATABASE={Config.AZURE_SQL_DATABASE};"
        f"UID={Config.AZURE_SQL_USERNAME};"
        f"PWD={Config.AZURE_SQL_PASSWORD}"
    )
    return pyodbc.connect(connection_string)

def insert_file_metadata(file_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO FileMetadata (FileName) VALUES (?)", (file_name,))
    conn.commit()
    cursor.close()
    conn.close()
