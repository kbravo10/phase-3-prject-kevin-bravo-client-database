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

#create a class doctor
class Doctor(Base):
    __tablename__ = 'doctors'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String())
    phone_number = Column(String())

    clients = relationship('Client')
    
    def __repr__(self):
        return f'Doctor {self.id}: {self.name},' +\
             f'phone # 1-{self.phone_number}, ' +\
             f'email: {self.email} \n'
    
class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    age = Column(Integer())

    medications = relationship('Med_times', back_populates='clients')
    doctor_id = Column(Integer(), ForeignKey('doctors.id'))

    def __repr__(self):
        return f'Client {self.id}: ' +\
            f'{self.name}, ' +\
            f'{self.age} years old, ' +\
            f'primary doctor id: {self.doctor_id} \n'


class Medication(Base):
    __tablename__ = 'medications'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    medication_use = Column(String())
    med_type = Column(String())

    clients = relationship('Med_times', back_populates='medications')

    def __repr__(self):
        return f'Medication {self.id}, ' +\
            f'{self.name}, medication description: \n' +\
            f'\t {self.medication_use} \n\n'

class Med_times(Base):
    __tablename__ = 'med_times'

    id = Column(Integer(), primary_key=True)
    time_slot = Column(String())
    dose = Column(String())

    signed_off = Column(ForeignKey('user.id'))
    client_id = Column(ForeignKey('clients.id'))
    medication_id = Column(ForeignKey('medications.id'))

    clients = relationship('Client', back_populates='medications')
    medications = relationship('Medication', back_populates='clients')
 
    def __repr__(self):
        return f'time {self.time_slot} ' +\
            f'- dose {self.dose}, '+\
            f'Client id: {self.client_id}, ' +\
            f'Medication id: {self.medication_id} \n'

class Employee(Base):
    __tablename__ = 'user'

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    username = Column(String())
    password = Column(String())

    med_times = relationship('Med_times')

    def __repr__(self):
        return f'Employee {self.id}: ' +\
            f'{self.name} \n'