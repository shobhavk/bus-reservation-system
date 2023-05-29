import os

class Settings:
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "MSService$234")
    MYSQL_SERVER = os.getenv("MYSQL_SERVER", "localhost")
    MYSQL_PORT = 3306
    MYSQL_DB = os.getenv("MYSQL_DB", "bus_reservation")
    DATABASE_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}:{MYSQL_PORT}/{MYSQL_DB}"

settings = Settings()
