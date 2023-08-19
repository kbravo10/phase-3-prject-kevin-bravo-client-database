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
from prettycli import red, green, yellow
from simple_term_menu import TerminalMenu
from  models import Doctor, Med_times, Client, Medication, Employee

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
        print(yellow('Welcome... Please choose an option: \n'))
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
        logged_in = False
        print('Please Log in: ')
        user_input = input(yellow('email: '))
        #find an owner by email 
        session = self.session_creator()
        employees = session.query(Employee).all()
        for employee in employees:
            if user_input == employee.username:
                logged_in = True
                self.current_user = employee
                self.home_screen()
        if logged_in == False:
            print(red('Email not valid...Please try again or EXIT'))
            time.sleep(1)
            self.start()

    #lets the user leave the program
    def exit(self):
        self.clear_screen()
        print('Thank you. Bye!')
        quit()

    #home screen that gives userr options of clients, medications and doctors
    def home_screen(self):
        self.clear_screen()
        #display welcome message and propmt the user to select a choice
        print(green('Welcome ')  + yellow(f'{self.current_user.name} \n'))
        options = ['Clients', 'Doctors', 'Medications',  'Medication Schedule', 'EXIT']
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
        elif options[menu_entry_index] == 'Medication Schedule':
            print('You have selected medication schedule.')
            time.sleep(1)
            self.handle_med_schedule_choice()
        elif options[menu_entry_index] == 'EXIT':
            self.exit()
        self.clear_screen()
    
    #handle option of clients from home screen
    def handle_client_choice(self):
        return_home = False
        while return_home == False:
            self.clear_screen()
            print(yellow('Choose an option: \n'))
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
                print(green('LIST OF ALL CLIENTS:'))
                for client in clients.all():
                    print(client)
            #Allow the user to enter a specific name and look for that clients information
            elif options[menu_entry_index] == 'Search by name':
                user_input = input(yellow('What is the clients name: '))
                client_filter_name = clients.filter(Client.name == user_input)
                self.clear_screen()
                if client_filter_name.count() != 0:
                    print(green('Client(s):'))
                    for client in client_filter_name:
                        print(client)
                        print(green(f'Medications perscribed: '))
                        for meds in client.medications:
                            print(meds.medications.name)
                        print(green(f'Medication schedule for {client.name}'))
                        for times in client.medications:
                            print(times)
                else:
                    print(red('There is no client with that name.'))
            #Allow the user to search a client with there id number
            elif options[menu_entry_index] == 'Search by ID':
                user_input = input(yellow('What is the clients id: '))
                client_filter_id = clients.filter(Client.id == user_input)
                if client_filter_id.count() != 0:
                    for client in client_filter_id:
                        print(client)
                else:
                    print(red('There is no client with that id.'))
            else:
                return_home = True
            time.sleep(1)
        self.home_screen()
        
    def handle_doctor_choice(self):
        return_home = False
        while return_home == False:
            self.clear_screen()
            #display options for doctor class and prompt user to select
            options = ['View all doctors', 'Search by name', 'Search by ID', 'Return to main screen']
            terminal_menu = TerminalMenu(options)
            menu_entry_index = terminal_menu.show()
            #create a session with the Doctor class
            session = self.session_creator()
            doctors = session.query(Doctor)
            self.clear_screen()
            #handle option to see all the doctors
            if options[menu_entry_index] == 'View all doctors':
                print(green('LIST OF ALL DOCTORS: '))
                for doctor in doctors.all():
                    print(doctor)
            #handle search by name
            elif options[menu_entry_index] == 'Search by name':
                user_input = input(yellow('Enter the doctors name: '))
                doctor_filter_name = doctors.filter(Doctor.name == user_input)
                if doctor_filter_name.count() != 0:
                    print(green('Doctor(s): '))
                    for doc in doctor_filter_name:
                        print(doc)
                else:
                    print(red('There is no doctor with that name on the database.'))
            elif options[menu_entry_index] == 'Search by ID':
                user_input = input(yellow('Enter the doctors ID: '))
                doctor_filter_id = doctors.filter(Doctor.id == user_input)
                if doctor_filter_id.count() != 0:
                    print(green('Doctor: '))
                    print(doctor_filter_id[0])
                else:
                    print(red('There is no doctor with this ID.'))
            else:
                return_home = True
            time.sleep(1)
        self.home_screen()

    def handle_medication_choice(self):
        return_home = False
        while return_home == False:
            self.clear_screen()
            #display options for medications class and prompt user to select
            options = ['View all medications', 'Search by name', 'Search by ID', 'Return to main screen']
            terminal_menu = TerminalMenu(options)
            menu_entry_index = terminal_menu.show()
            #create a session with the Doctor class
            session = self.session_creator()
            medications = session.query(Medication)
            self.clear_screen()
            #print all of the medications if user wants to view all medications
            if options[menu_entry_index] == 'View all medications':
                print(green('LIST OF ALL MEDICATIONS: \n'))
                for med in medications.all():
                    print(med)
            #Allow the user to enter a specific name and look for that medications information
            elif options[menu_entry_index] == 'Search by name':
                user_input = input(yellow('What is the medications name: '))
                medication_filter_name = medications.filter(Medication.name == user_input)
                self.clear_screen()
                if medication_filter_name.count() != 0:
                    print(green('Medications(s):'))
                    for meds in medication_filter_name:
                        print(meds)
                        print(green(f'List of clients on Medication- {meds.name}:'))
                        for client in meds.clients:
                            print(f'{client.clients.name}, ID: {client.clients.id}')
                else:
                    print(red('There is no medication with that name.'))
            #Allow the user to search a medications with there id number
            elif options[menu_entry_index] == 'Search by ID':
                user_input = input(yellow('What is the medication id: '))
                medication_filter_id = medications.filter(Medication.id == user_input)
                if medication_filter_id.count() != 0:
                    print(medication_filter_id[0])
                else:
                    print(red('There is no medication with that id.'))
            else:
                return_home = True
            time.sleep(1)
        self.home_screen()

    def handle_med_schedule_choice(self):
        return_home = False
        while return_home == False:
            self.clear_screen()
            #display options for user to choose medication schedule
            options = ['Sign Off medication time slot', 'View medication schedule', 'Filter by time', 'Return to main screen']
            terminal_menu = TerminalMenu(options)
            menu_entry_index = terminal_menu.show()
            #create a session with the Doctor class
            session = self.session_creator()
            medications = session.query(Med_times)
            self.clear_screen()

            if options[menu_entry_index] == 'View medication schedule':
                print(green('MEDICATION SCHEDULE: '))
                for times in medications.all():
                    print(times)

            elif options[menu_entry_index] == 'Filter by time':
                user_input = input(yellow('What time slot would you want to view ( 16:00 = 04:00 apm): '))
                med_times_filter = medications.filter(Med_times.time_slot == user_input)
                print(green(f'List of {user_input}:'))
                for times in med_times_filter:
                    print(times)

            elif options[menu_entry_index] == 'Sign Off medication time slot':
                print(green('Enter the client information and the time slot you want to sign off.'))
                client_id = input(yellow('Enter a clients ID: '))
                time_slot = input(yellow('Enter the time: '))
                x = medications.filter(Med_times.client_id == client_id)
                y = x.filter(Med_times.time_slot == time_slot)
                print(y[0])

            else:
                return_home = True
            time.sleep(1)
        self.home_screen()

app = Cli()
app.start()