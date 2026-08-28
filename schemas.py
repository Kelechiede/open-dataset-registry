from pydantic import BaseModel
from typing import Optional


class AdminRegister(BaseModel):
    username: str
    email:    str
    password: str


class DatasetCreate(BaseModel):
    name:        str
    source:      str
    format:      str
    size:        str
    domain:      str
    description: Optional[str] = None
    tags:        Optional[str] = None
    url:         Optional[str] = None


class DatasetUpdate(BaseModel):
    name:        Optional[str] = None
    source:      Optional[str] = None
    format:      Optional[str] = None
    size:        Optional[str] = None
    domain:      Optional[str] = None
    description: Optional[str] = None
    tags:        Optional[str] = None
    url:         Optional[str] = None