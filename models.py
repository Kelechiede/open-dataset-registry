from sqlalchemy import Column, Integer, String, Text
from database import Base


class Admin(Base):
    __tablename__ = "admins"

    id       = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    email    = Column(String(200), unique=True, nullable=False)
    password = Column(String(500), nullable=False)


class Dataset(Base):
    __tablename__ = "datasets"

    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String(200), nullable=False)
    source      = Column(String(300), nullable=False)
    format      = Column(String(50),  nullable=False)
    size        = Column(String(50),  nullable=False)
    domain      = Column(String(100), nullable=False)
    description = Column(Text,        nullable=True)
    tags        = Column(String(300), nullable=True)
    url         = Column(String(500), nullable=True)