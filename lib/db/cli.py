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

class Cli():
    #variable that keeps track of person logged in
    current_user = None

    def session_creator(self):
        engine = create_engine('sqlite:///client_database.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    #method start to prompt the user how to start and the options
    def start(self):
        self.clear_screen()
        print('Welcome... Please choose an option: \n')

        #use simple term menu to get user input for choice to log in or exit
        options = ['Login', 'Exit']
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        #depending the users choice run the if statement
        if menu_entry_index == 1:
            self.exit()
        else:
            self.login()
        
        self.clear_screen()
    
    #method to help with the cluter by printing empty lines
    def clear_screen(self):
        print('\n' *5)

    #lets the user login if login was chosen
    def login(self):
        self.clear_screen()
        print('Please Log in: ')
        user_input = input('email: ')
        self.home_screen(user_input)

    #lets the user leave the program
    def exit(self):
        self.clear_screen()
        print('Thank you. Bye!')

    #home screen that gives userr options of clients, medications and doctors
    def home_screen(self, user):
        self.clear_screen()
        print(f'Welcome {user}')
        options = ['Clients', 'Medications', 'Doctors', 'Medication Schedule']
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        if options[menu_entry_index] == 'Clients':
            self.handle_client_choice()

        self.clear_screen()
    
    #handle option of clients from home screen
    def handle_client_choice(self):
        print('You have chosen clients')
        session = self.session_creator()
        client = Client(
            name = 'kevin bravo',
            age = 29,
            doctor_id = 2
        )
        session.add(client)
        session.commit()
        session.close()


app = Cli()
app.start()