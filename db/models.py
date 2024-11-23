from sqlalchemy import Integer, String,DateTime
from sqlalchemy.orm import Mapped,mapped_column
from datetime import datetime
from db.Base import Base

class Link(Base):
    __tablename__ = 'Link'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True,index=True)
    url: Mapped[str] = mapped_column(String, index=True,nullable=False,unique=True)
    DteTime: Mapped[str] = mapped_column(DateTime, index=True,nullable=False,default=datetime.now())

