from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, String, Integer
engine = create_engine('sqlite:///taskmanager.db', echo=True)

SessionLocal = sessionmaker(bing=engine)


class Base(DeclarativeBase):
    pass
