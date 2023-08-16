#import all necessary libraries from sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from faker import Faker

#import random to random fill values
import random
import ipdb
from prettycli import red, green
from simple_term_menu import TerminalMenu
from  models import Doctor, Med_times, Client, Medication

Base = declarative_base()

if __name__ == "__main__":
    
    #method start to prompt the user how to start and the options
    def start():
        print('\n' * 10)

        print('Welcome... Please choose an option: \n')
        options = ['Clients', 'Medications', 'Doctors', 'Medication Times']
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(green(f'You have selected {options[menu_entry_index]}'))

        print('\n' *5)

    def handle_user_input():
        pass
    

    start()