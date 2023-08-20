import sessions
from prettycli import red, yellow, green
import time
from simple_term_menu import TerminalMenu
import helpers

from  db.models import Doctor, Med_times, Client, Medication, Employee

def handle_add_client():
    new_client_name = input(yellow('New client name: '))
    new_client_age = helpers.check_if_integer('New client age: ')
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
    
    new_time_slot = input(yellow('Choose a time slot: '))
    new_dose = input(yellow('Enter a new dose amout: '))


    new_client_id = input(yellow('Enter the clients ID: '))
    new_med_id = input(yellow('Enter the ID of the medication: '))
    sign_off = input(yellow('Are you signing off this slot? Y/N: '))
    new_sign_off = ''
    if sign_off == 'y'or 'Y'or'Yes'or 'yes':
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