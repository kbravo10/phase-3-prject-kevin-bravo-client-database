import sessions
from prettycli import red, yellow, green

from  db.models import Doctor, Med_times, Client, Medication, Employee

def handle_add_client():
    new_client_name = input('New client name: ')
    new_client_age = input('New client age: ')
    new_client_doc = input('What is the new clients primary doctor ID: ')
    new_client = Client(
        name = new_client_name,
        age = new_client_age,
        doctor_id = new_client_doc,
    )
    session = sessions.session
    session.add(new_client)
    session.commit()

def handle_add_med_times():
    
    new_time_slot = input('Choose a time slot: ')
    new_dose = input('Enter a new dose amout: ')
    new_client_id = input('Enter the clients ID: ')
    new_med_id = input('Enter the ID of the medication')
    new_sign_off = input()
    y = Med_times(
        time_slot = '4:00',
        dose = '4',
        signed_off = 1,
        client_id = 3,
        medication_id = 2,
    )
    sess = sessions.session
    # sess.add(y)
    # sess.commit()

    t = med_time_sess.filter(Med_times.time_slot == '4:00')
    p = t.filter(Med_times.client_id == 6)
    print(p[0])
    p[0].signed_off = 2
    sess.commit()