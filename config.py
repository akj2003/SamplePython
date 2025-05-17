import os

class Config:
    AZURE_SQL_SERVER = os.getenv("AZURE_SQL_SERVER", "tcp:dms-sample.database.windows.net,1433")
    AZURE_SQL_DATABASE = os.getenv("AZURE_SQL_DATABASE", "RecieptDoc-db")
    AZURE_SQL_USERNAME = os.getenv("AZURE_SQL_USERNAME", "achuj2003")
    AZURE_SQL_PASSWORD = os.getenv("AZURE_SQL_PASSWORD", "AchuJ@2003")
    AZURE_SQL_DRIVER = os.getenv("AZURE_SQL_DRIVER", "{ODBC Driver 17 for SQL Server}")
