#import all necessary libraries from sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import ipdb

#import faker to fill database with random but correct type values
from faker import Faker

#import classes from models
from models import Client, Doctor, Medication, Med_times, Employee

#import random to random fill values
import random

Base = declarative_base()

if __name__ == '__main__':
    #create the session object
    engine = create_engine('sqlite:///client_database.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    #remove data from databases 
    session.query(Client).delete()
    session.query(Doctor).delete()
    session.query(Medication).delete()
    session.query(Med_times).delete()
    session.query(Employee).delete()

    #create an instace of Faker
    fake = Faker()


    #add doctor table and create sql
    doctors = []
    for i in range(2):
        doc = Doctor(
            name = fake.unique.name(),
            email = fake.unique.email(),
            phone_number = str(f'{random.randint(100, 999)}-{random.randint(1000, 9999)}')
        )
        #add and commit clients
        session.add(doc)
        session.commit()
        doctors.append(doc)

    #add data into the Client class and create a sql table
    clients = []
    for i in range(5):
        doc = random.choice(doctors)
        client = Client(
            name = fake.unique.name(),
            age = random.randint(1, 100),
            doctor_id = doc.id,
            )
        session.add(client)
        session.commit()
        clients.append(client)

    #add data to medication class
    medications = []
    for i in range(10):
        med = Medication(
            name = fake.unique.name(),
            medication_use = fake.unique.sentence(),
            med_type = fake.unique.name()
        )
        session.add(med)
        session.commit()
        medications.append(med)


    employees = []
    for i in range(4):
        employee = Employee(
            name = fake.unique.name(),
            username = fake.unique.email(),
            password = fake.unique.name(),
        )
        session.add(employee)
        session.commit()
        employees.append(employee)

    med_times = []
    for client in clients:
        for i in range(random.randint(2,6)):
            medication = random.choice(medications)
            emplee = random.choice(employees)
            times = Med_times(
                time_slot = str(4 * (i + 1)) + ':00',
                dose = str(random.randint(5,20))+ ' mm',
                signed_off = emplee.id,
                client_id = client.id,
                medication_id = medication.id,
            )

            med_times.append(times)

    session.bulk_save_objects(med_times)
    session.commit()

    session.close()
ipdb.set_trace()