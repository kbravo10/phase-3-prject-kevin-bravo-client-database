#import all necessary libraries from sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from faker import Faker

#import random to random fill values
import random
import time
import pandas as pd
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
    
    #method to help with the cluter by printing empty lines
    def clear_screen(self):
        print('\n' * 3)

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
    
   

    #lets the user login if login was chosen
    def login(self):
        self.clear_screen()
        print('Please Log in: ')
        user_input = input('email: ')
        self.home_screen()

    #lets the user leave the program
    def exit(self):
        self.clear_screen()
        print('Thank you. Bye!')

    #home screen that gives userr options of clients, medications and doctors
    def home_screen(self):
        self.clear_screen()
        #display welcome message and propmt the user to select a choice
        print(f'Welcome')
        options = ['Clients', 'Doctors', 'Medications',  'Medication Schedule']
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        #if the user chooses clients then take them to the handle_client_choice method
        if options[menu_entry_index] == 'Clients':
            print('You have chosen clients')
            time.sleep(1)
            self.handle_client_choice()
        #the user chooses doctor take them to the handle_doctor_method
        elif options[menu_entry_index] == 'Doctors':
            print('You have chosen doctors.')
            time.sleep(1)
            self.handle_doctor_choice()
        #the user selects medication, take them to handle_medication_choice
        elif options[menu_entry_index] == 'Medications':
            print('You have chosen Medication.')
            time.sleep(1)
            self.handle_medication_choice()
        #user selects Medication schedule
        else:
            print('You have selected medication schedule.')
            time.sleep(1)
            self.handle_med_schedule_choice()

        self.clear_screen()
    
    #handle option of clients from home screen
    def handle_client_choice(self):
        self.clear_screen()
        print('Choose an option: \n')
        #display the users option when client is chosen 
        options = ['View all clients', 'Search by name', 'Search by ID', 'Return to main screen']
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        #call session_creater to start a sesseion
        session = self.session_creator()
        clients = session.query(Client)
        self.clear_screen()

        #print all of the clients if user wants to view all clients
        if options[menu_entry_index] == 'View all clients':
            print('list of all clients')
            for client in clients.all():
                print(client)
            time.sleep(2)
            self.handle_client_choice()

        #Allow the user to enter a specific name and look for that clients information
        elif options[menu_entry_index] == 'Search by name':
            user_input = input('What is the clients name: ')
            client_filter_name = clients.filter(Client.name == user_input)
            self.clear_screen()
            if client_filter_name.count() != 0:
                print('Client(s):')
                for client in client_filter_name:
                    print(client)
                    print(f'medication times: \n{client.medications}')
            
            else:
                print(red('There is no client with that name.'))
        #Allow the user to search a client with there id number
        elif options[menu_entry_index] == 'Search by ID':
            user_input = input('What is the clients id: ')
            client_filter_id = clients.filter(Client.id == user_input)
            if client_filter_id.count() != 0:
                print(client_filter_id[0])
            else:
                print(red('There is no client with that id.'))
        else:
            self.home_screen()
        

    def handle_doctor_choice(self):
        self.clear_screen()

        #display options for doctor class and prompt user to select
        options = ['View all doctors', 'Search by name', 'Search by ID']
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        
        #create a session with the Doctor class
        session = self.session_creator()
        doctors = session.query(Doctor)
        self.clear_screen()

        #handle option to see all the doctors
        if options[menu_entry_index] == 'View all doctors':
            print(doctors.all())
        #handle search by name
        elif options[menu_entry_index] == 'Search by name':
            user_input = input('Enter the doctors name: ')
            doctor_filter_name = doctors.filter(Doctor.name == user_input)

            if doctor_filter_name.count() != 0:
                for doc in doctor_filter_name:
                    print(doc)
            else:
                print(red('There is no doctor with that name on the database.'))
        elif options[menu_entry_index] == 'Search by ID':
            user_input = input('Enter the doctors ID: ')
            doctor_filter_id = doctors.filter(Doctor.id == user_input)
            
            if doctor_filter_id.count() != 0:
                print(doctor_filter_id[0])
            else:
                print(red('There is no doctor with this ID.'))
    def handle_medication_choice(self):
        self.clear_screen()

        #display options for medications class and prompt user to select
        options = ['View all medications', 'Search by name', 'Search by ID']
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        
        #create a session with the Doctor class
        session = self.session_creator()
        medications = session.query(Medication)
        self.clear_screen()

        #print all of the medications if user wants to view all medications
        if options[menu_entry_index] == 'View all medications':
            print('list of all medications')
            for med in medications.all():
                print(med)
        #Allow the user to enter a specific name and look for that medications information
        elif options[menu_entry_index] == 'Search by name':
            user_input = input('What is the medications name: ')
            medication_filter_name = medications.filter(Medication.name == user_input)
            self.clear_screen()
            if medication_filter_name.count() != 0:
                print('Medications(s):')
                for meds in medication_filter_name:
                    print(meds)
            else:
                print(red('There is no medication with that name.'))
        #Allow the user to search a medications with there id number
        elif options[menu_entry_index] == 'Search by ID':
            user_input = input('What is the medication id: ')
            medication_filter_id = medications.filter(Medication.id == user_input)
            if medication_filter_id.count() != 0:
                print(medication_filter_id[0])
            else:
                print(red('There is no medication with that id.'))
    
    def handle_med_schedule_choice(self):
        self.clear_screen()

        #display options for user to choose medication schedule
        options = ['View medication schedule', 'Filter by time']
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        
        #create a session with the Doctor class
        session = self.session_creator()
        medications = session.query(Med_times)
        self.clear_screen()

        if options[menu_entry_index] == 'View medication schedule':
            for time in medications.all():
                print(time)
        
        elif options[menu_entry_index] == 'Filter by time':
            user_input = input('What time slot would you want to view ( 16:00 = 04:00 apm): ')
            med_times_filter = medications.filter(Med_times.time_slot == user_input)
            for times in med_times_filter:
                print(times)




app = Cli()
app.start()