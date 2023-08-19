import sessions

from  db.models import Doctor, Med_times, Client, Medication, Employee

def handle_add_client():
    print('in create')
    client_sess = sessions.create_client_session()
    new_client = Client(
        name = 'Kevin Bravo',
        age = 29,
        doctor_id = 1,
    )
    session = sessions.session
    session.add(new_client)
    session.commit()

def handle_add_med_times():
    print('add med_time')
    # create session.query(Med_times)
    med_time_sess = sessions.create_med_times_session()
    
    x = med_time_sess.first().clients
    
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

    

handle_add_med_times()


