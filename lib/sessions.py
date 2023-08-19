#import all necessary libraries from sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from  db.models import Doctor, Med_times, Client, Medication, Employee

Base = declarative_base()
engine = create_engine('sqlite:///db/client_database.db')
Session = sessionmaker(bind=engine)
session = Session()

def session_create():
    return session

def create_client_session():
    return session.query(Client)

def create_med_times_session():
    return session.query(Med_times)

def create_doctor_session():
    return session.query(Doctor)

def create_medication_session():
    return session.query(Medication)

def create_employee_session():
    return session.query(Employee)