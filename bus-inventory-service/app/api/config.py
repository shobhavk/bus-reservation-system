import os

class Settings:
    
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_SERVER = os.getenv("MYSQL_SERVER")
    MYSQL_PORT = 3306 # default MYSQL port is 3306
    MYSQL_DB = os.getenv("MYSQL_DB")
    DATABASE_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}:{MYSQL_PORT}/{MYSQL_DB}"

settings = Settings()