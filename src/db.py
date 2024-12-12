from dotenv import load_dotenv
from sqlalchemy import create_engine

import os

load_dotenv()
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_debug = os.getenv("DB_DEBUG").lower() == "true"
engine = create_engine(
    f"postgresql+psycopg://{db_user}:{db_password}@localhost/amora", echo=db_debug
)
