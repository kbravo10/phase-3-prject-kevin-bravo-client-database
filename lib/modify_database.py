import sessions
from prettycli import red, yellow, green
import time
from simple_term_menu import TerminalMenu
import helpers
import validate

from  db.models import Doctor, Med_times, Client, Medication, Employee

def handle_add_client():
    new_client_name = input(yellow('New client name: '))
    new_client_age = helpers.check_if_integer('New client age: ')
    new_client_age = int(new_client_age)
    doc_options = sessions.create_doctor_session()
    print(yellow('What is the new clients primary doctor: '))
    options = []
    for i in doc_options:
        options.append(i.name)
    
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    new_client_doc = doc_options.filter(Doctor.name == options[menu_entry_index])[0].id
    new_client = Client(
        name = new_client_name,
        age = new_client_age,
        doctor_id = new_client_doc,
    )
    session = sessions.session
    session.add(new_client)
    session.commit()
    print(green('New client has been added.'))
    time.sleep(1)

def handle_add_med_times(user):
    
    new_time_slot = helpers.time_slots()
    new_dose = 'NA'
    new_client_id = validate.validate_client_id()
    new_med_id = input(yellow('Enter the ID of the medication: '))
    sign_off = input(yellow('Are you signing off this slot? Y/N: '))
    new_sign_off = 'NOT SIGNED OFF'
    if sign_off == 'y'or sign_off =='Y'or sign_off =='Yes'or sign_off =='yes':
        new_sign_off = user
    new_medicatiion_slot = Med_times(
        time_slot = new_time_slot,
        dose = new_dose,
        signed_off = new_sign_off,
        client_id = new_client_id,
        medication_id = new_med_id,
    )
    sess = sessions.session
    sess.add(new_medicatiion_slot)
    sess.commit()
    print(green('The time slot has been added. '))
    time.sleep(1)

def remove_client():
    session = sessions.session_create()
    print('Enter the clients information you wish to remove: ')
    client_id = input('Enter client ID: ')
    client = sessions.create_client_session().filter(Client.id == client_id)
    if client.count() != 0:
        time_slot = sessions.create_med_times_session().filter(Med_times.client_id == client_id)
        for times in time_slot:
            session.delete(times)
            session.commit()
        
        session.delete(client[0])
        session.commit()
        print(green('The client has been removed, along with all the medicine time slots.'))
    else:
        print(red('The client is not in the database.'))



def remove_med_time():
    print('Enter the Medication schedule information you wish to remove: ')
    med_time = helpers.time_slots()
    client_id = input('Enter the clients ID for time slot: ')
    client = sessions.create_med_times_session().filter(Med_times.client_id == client_id)
    if client.count() != 0:
        time_slot = client.filter(Med_times.time_slot == med_time)
        if time_slot.count() != 0:
            session = sessions.session_create()
            session.delete(time_slot[0])
            session.commit()
            print(green('The time slot on the schedule has been removed'))
        else:
            print(red('The time slot is not in the database.'))
    else:
        print(red('The time slot is not in the database.'))

# s = sessions.create_medication_session()
# print(s[1].clients.id)