import sessions
from prettycli import red, yellow, green
import time
from simple_term_menu import TerminalMenu
import helpers

from  db.models import Doctor, Med_times, Client, Medication, Employee

def validate_client_id():
    valid = False
    while valid == False:
        user_input = helpers.check_if_integer('Enter clients id: ')
        validate_client = sessions.create_client_session().filter(Client.id == user_input)
        if validate_client.count() != 0:
            return int(user_input)
        else:
            print(red('There is no client with that id.'))

def validate_medication_id():
    valid = False
    while valid == False:
        user_input = helpers.check_if_integer('Enter medication id: ')
        validate_client = sessions.create_medication_session().filter(Medication.id == user_input)
        if validate_client.count() != 0:
            return int(user_input)
        else:
            print(red('There is no medication with that id.'))
