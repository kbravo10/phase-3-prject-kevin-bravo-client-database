from sqlalchemy import ForeignKey, Table, Integer, Column, String
from sqlalchemy.orm import relationship, backref, declarative_base

Base = declarative_base()
#create a class doctor
class Doctor(Base):
    __tablename__ = 'doctors'

    id = Column(Integer(), primary_key=True)
    email = Column(String())
    phone_number = Column(String())
    
class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    age = Column(Integer())


class Medication(Base):
    __tablename__ = 'medications'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    medication_use = Column(String())
    med_type = Column(String())