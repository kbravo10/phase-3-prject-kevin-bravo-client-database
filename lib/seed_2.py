#import all necessary libraries from sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#import faker to fill database with random but correct type values
from faker import Faker

#import classes from models
from db.models import Client, Doctor, Medication, Med_times, Employee
import sessions

#import random to random fill values
import random

Base = declarative_base()

if __name__ == '__main__':
    session = sessions.session_create()

    #remove data from databases 
    sessions.create_client_session().delete()
    sessions.create_doctor_session().delete()
    sessions.create_medication_session().delete()
    sessions.create_med_times_session().delete()
    sessions.create_employee_session().delete()

    #create an instace of Faker
    fake = Faker()

    #add doctor table and create sql
    doctors = []
    for i in range(3):
        doc = Doctor(
            name = fake.unique.name(),
            email = fake.unique.email(),
            phone_number = str(f'{random.randint(100, 999)}-{random.randint(1000, 9999)}')
        )
        session.add(doc)
        session.commit()
        doctors.append(doc)

    #add data to medication class
    meds = {
        'Adderall':'Adderall is used to treat attention deficit hyperactivity disorder (ADHD) and narcolepsy.',
        'Atorvastatin':"It's used to help lower cholesterol and fat levels in your blood",
        'Levothyroxine':"Levothyroxine is a man-made hormone that is used to treat hypothyroidism. Hypothyroidism is a condition where your thyroid doesn't produce enough thyroid hormone naturally.",
        'Lisinopril':"Lisinopril is a type of angiotensin-converting enzyme (ACE) inhibitor used to treat high blood pressure.",
        'Metformin' : "Metformin is used to treat type 2 diabetes",
        'Albuterol' :"Albuterol is used to treat bronchospasm, which is when your airways spasm and tighten and make it hard to breathe.",
        'Gabapentin' : "Gabapentin works in your brain to prevent seizures and relieve certain types of pain. It is used to treat epilepsy, nerve pain after shingles, and moderate to severe restless leg syndrome. It's also sometimes used to treat other types of nerve pain, fibromyalgia, hot flashes after menopause, anxiety, mood disorders, irritable bowel syndrome (IBS), alcohol withdrawal, migraines, itching, and insomnia.",
        'Omeprazole' : "Omeprazole is used to treat conditions that result from too much acid in your stomach.",
        'Losartan' : "Losartan is the fourth in the top 10 medicines used to treat high blood pressure."
    }
    medications = []
    for i in range(len(meds)):
        med = Medication(
            name = [i for i in meds][i],
            medication_use = [values for values in meds.values()][i],
            med_type = 'NA'
        )
        session.add(med)
        session.commit()
        medications.append(med)

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

    emails = [
        'userOne@google.com',
        'userTwo@google.com',
        'userThree@google.com',
        'userFour@google.com',
    ]
    employees = []
    for i in range(len(emails)):
        employee = Employee(
            name = fake.unique.name(),
            username = emails[i],
            password = fake.unique.name(),
        )
        session.add(employee)
        session.commit()
        employees.append(employee)
    
    med_times = []
    for client in clients:
        for i in range(random.randint(2,5)):
            medication = random.choice(medications)
            emplee = random.choice(employees)
            times = Med_times(
                time_slot = str(4 * (i + 1)) + ':00',
                dose = 'NA',
                signed_off = 'NOT SIGNED OFF',
                client_id = client.id,
                medication_id = medication.id,
            )

            med_times.append(times)

    session.bulk_save_objects(med_times)
    session.commit()

    session.close()

import ipdb;ipdb.set_trace()


