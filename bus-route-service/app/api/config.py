import os
# from dotenv import load_dotenv

# from pathlib import Path
# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)

class Settings:
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    # MYSQL_SERVER = 'host.docker.internal'
    MYSQL_SERVER = os.getenv("MYSQL_SERVER")
    MYSQL_PORT = 3306 # default MYSQL port is 3306
    MYSQL_DB = os.getenv("MYSQL_DB")
    DATABASE_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}:{MYSQL_PORT}/{MYSQL_DB}"
    print(DATABASE_URL,f"This is user {MYSQL_USER} {MYSQL_PASSWORD} {MYSQL_PORT} {MYSQL_DB}")
settings = Settings()


