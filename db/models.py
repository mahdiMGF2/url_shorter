from sqlalchemy import create_engine,Column, Integer, String,DateTime,CheckConstraint
from sqlalchemy.orm import declarative_base,Mapped,mapped_column,sessionmaker
from datetime import datetime
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db = create_engine(f"sqlite:///{BASE_DIR}/database.db")
Base = declarative_base()
session = sessionmaker(bind=db)
session = session()

class Link(Base):
    __tablename__ = 'Link'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True,index=True)
    url: Mapped[str] = mapped_column(String, index=True,nullable=False,unique=True)
    DteTime: Mapped[str] = mapped_column(DateTime, index=True,nullable=False,default=datetime.now())


Base.metadata.create_all(db)