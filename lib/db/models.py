from sqlalchemy import ForeignKey, Table, Integer, Column, String
from sqlalchemy.orm import relationship, backref, declarative_base

Base = declarative_base()
