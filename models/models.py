from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class TestModel(Base):
    __tablename__ = "test_table"
    __table_args__ = {"schema": "test"}
    id = Column(Integer, primary_key=True)
    message = Column(String(255))
