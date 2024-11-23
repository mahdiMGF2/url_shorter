from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
import os

# home dir db
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# connect db
db = create_engine(f"sqlite:///{BASE_DIR}/database.db")


Base = declarative_base()
session = sessionmaker(bind=db)
session = session()
