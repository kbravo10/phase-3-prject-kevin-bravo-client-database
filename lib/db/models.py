from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Integer, Column, String, DateTime, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

metadata = MetaData(naming_convention = convention)

engine = create_engine('sqlite:///client_database.db')

Base = declarative_base(metadata = metadata)

client_medication = Table(
    'clent_medication',
    Base.metadata,
    Column('client_id', ForeignKey('clients.id'), primary_key=True),
    Column('medication_id', ForeignKey('medications.id'), primary_key=True),
)

#create a class doctor
class Doctor(Base):
    __tablename__ = 'doctors'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String())
    phone_number = Column(String())

    clients = relationship('Client')
    
    def __repr__(self):
        return f'Doctor {self.id}: {self.name}, #{self.phone_number}'
    
class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    age = Column(Integer())

    medications = relationship('Medication', secondary=client_medication, back_populates='clients')
    doctor_id = Column(Integer(), ForeignKey('doctors.id'))

    def __repr__(self):
        return f'Client {self.id}: ' +\
            f'{self.name}' +\
            f'{self.age} years old\n'


class Medication(Base):
    __tablename__ = 'medications'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    medication_use = Column(String())
    med_type = Column(String())

    clients = relationship('Client', secondary=client_medication, back_populates='medications')

    def __repr__(self):
        return f'Medication {self.id}'

class Med_times(Base):
    __tablename__ = 'med_times'

    id = Column(Integer(), primary_key=True)
    time_slot = Column(String())
    dose = Column(String())
    signed_off = Column(DateTime(), onupdate=func.now)

    client_id = Column(Integer(), ForeignKey('clients.id'))
    medication_id = Column(Integer(), ForeignKey('medications.id'))
 
    def __repr__(self):
        return f'{self.time_slot} - dose {self.time_slot}, Client id: {self.client_id} - Medication id: {self.medication_id}'