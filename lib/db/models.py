from sqlalchemy import ForeignKey, Table, Integer, Column, String
from sqlalchemy.orm import relationship, backref, declarative_base

Base = declarative_base()
#create a class doctor
class Doctor(Base):
    __tablename__ = 'doctors'

    id = Column(Integer(), primary_key=True)
    email = Column(String())
    phone_number = Column(String())

    def __repr__(self):
        return f'Doctor {self.id}'
    
class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    age = Column(Integer())

    def __repr__(self):
        return f'Client {self.id}: ' +\
            f'{self.name}' +\
            f'{self.age} years old \n'


class Medication(Base):
    __tablename__ = 'medications'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    medication_use = Column(String())
    med_type = Column(String())

    def __repr__(self):
        return f'Medication {self.id}'