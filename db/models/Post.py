from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    author = Column(String(20))
    title = Column(String(50))
    body = Column(String(200))
    publish_date = Column(Integer)
