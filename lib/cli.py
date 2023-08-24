
#import random to random fill values
import time
from prettycli import red, green, yellow
from simple_term_menu import TerminalMenu
from  db.models import Doctor, Med_times, Client, Medication, Employee
import art
import modify_database as modify
import sessions
import validate
import helpers

class Cli():
    #variable that keeps track of person logged in
    current_user = None
    
    #method to help with the cluter by printing empty lines
    def clear_screen(self):
        print('\n' * 60)

    #method start to prompt the user how to start and the options
    def start(self):
        self.clear_screen()
        art.tprint('DOCTOR-KEVIN-HOUSE')
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
        art.tprint('EMPLOYEE-LOGIN')
        print('Please Log in: ') 
        print('FOR TESTING YOU CAN USE: ')
        print(green('userOne@google.com'))
        user_input = input(yellow('email: '))
       
        #find an owner by email 
        employees = sessions.create_employee_session().all()
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
        sessions.session_create().close()
        quit()

    #home screen that gives userr options of clients, medications and doctors
    def home_screen(self):
        self.clear_screen()
        art.tprint('HOME')
        #display welcome message and propmt the user to select a choice
        print(green('Welcome ')  + yellow(f'{self.current_user.name} \n'))
        options = ['Clients', 'Doctors', 'Medications',  'Medication Schedule/Sign off time sheet', 'ADD/REMOVE INFORMATION', 'LOGOUT', 'EXIT']
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
        elif options[menu_entry_index] == 'Medication Schedule/Sign off time sheet':
            print('You have selected medication schedule.')
            time.sleep(1)
            self.handle_med_schedule_choice()
        #user selects to add a client or a medication time slot
        elif options[menu_entry_index] == 'ADD/REMOVE INFORMATION':
            self.handle_modify_info()
        #Lets the user log out of the class under there information
        elif options[menu_entry_index] == 'LOGOUT':
            print(f'Logging out. Bye {self.current_user.name}!')
            time.sleep(1)
            self.start()
        #lets the user quit the program
        elif options[menu_entry_index] == 'EXIT':
            self.exit()
        self.clear_screen()
    
    #handle option of clients from home screen
    def handle_client_choice(self):
        return_home = False
        #while loop to loop on method until user ready to leave
        while return_home == False:
            self.clear_screen()
            art.tprint("CLIENT'S")
            print(yellow('Choose an option: \n'))
            #display the users option when client is chosen 
            options = ['View all clients', 'Search by name', 'Search by ID', 'Return to main screen']
            terminal_menu = TerminalMenu(options)
            menu_entry_index = terminal_menu.show()
            #call session_creater to start a sesseion
            clients = sessions.create_client_session()
            self.clear_screen()
            #print all of the clients if user wants to view all clients
            if options[menu_entry_index] == 'View all clients':
                print(green('LIST OF ALL CLIENTS:'))
                for client in clients.all():
                    print(client)
            #Allow the user to enter a specific name and look for that clients information
            elif options[menu_entry_index] == 'Search by name':
                #get the user input and validate the users input name
                client_filter_name = validate.search_by('Client', Client)
                #display the client info and display all medication related to that client
                print('\n')
                print(green('Client(s):'))
                for client in client_filter_name:
                    print(client)
                    print(green(f'Medications perscribed: '))
                    for meds in client.medications:
                        print(meds.medications.name)
                    print('\n')
                    print(green(f'Medication schedule for {client.name}'))
                    for times in client.medications:
                        print(times)
            #Allow the user to search a client with there id number
            elif options[menu_entry_index] == 'Search by ID':
                client_filter_id = validate.validate_id('Client', Client)
                if client_filter_id != None:
                    print('\n')
                    print(green('Client: '))
                    for client in client_filter_id:
                        print(client)
                        print(green(f'Medications perscribed: '))
                        for meds in client.medications:
                            print(meds.medications.name)
                        print(green(f'Medication schedule for {client.name}'))
                        for times in client.medications:
                            print(times)
            #breaks the loop and lets user go back to home screen
            else:
                return_home = True
            input(yellow('Press any key When ready.'))
        self.home_screen()
        
    def handle_doctor_choice(self):
        return_home = False
        while return_home == False:
            self.clear_screen()
            art.tprint("DOCTOR'S")
            print(yellow('Choose an option: '))
            #display options for doctor class and prompt user to select
            options = ['View all doctors', 'Search by name', 'Search by ID', 'Return to main screen']
            terminal_menu = TerminalMenu(options)
            menu_entry_index = terminal_menu.show()
            #create a session with the Doctor class
            doctors = sessions.create_doctor_session()
            self.clear_screen()
            #handle option to see all the doctors
            if options[menu_entry_index] == 'View all doctors':
                print(green('LIST OF ALL DOCTORS: '))
                for doctor in doctors.all():
                    print(doctor)
            #handle search by name
            elif options[menu_entry_index] == 'Search by name':
                #get the user input and validate the users input name for doctor
                doctor_filter_name = validate.search_by('Doctor', Doctor)
                print('\n')
                print(green('Doctor(s): '))
                for doc in doctor_filter_name:
                    print(doc)
                    print(green('List of clients'))
                    for client in doc.clients:
                        print(f'{client.name}, ID: {client.id}')
            #handle the user wanting to search by id
            elif options[menu_entry_index] == 'Search by ID':
                doctor_filter_id = validate.validate_id('Doctor', Doctor)
                if doctor_filter_id != None:
                    print(green('Doctor: '))
                    print(doctor_filter_id[0])
                    print(green('List of clients'))
                    for client in doctor_filter_id[0].clients:
                        print(f'{client.name}, ID: {client.id}')
            #breaks loop and allows the user to return to main screen
            else:
                return_home = True
            input(yellow('Press any key When ready.'))
        self.home_screen()

    def handle_medication_choice(self):
        return_home = False
        while return_home == False:
            self.clear_screen()
            art.tprint("MEDICATION'S")
            print(yellow('Choose an option: '))
            #display options for medications class and prompt user to select
            options = ['View all medications', 'Search by name', 'Search by ID', 'Return to main screen']
            terminal_menu = TerminalMenu(options)
            menu_entry_index = terminal_menu.show()
            #create a session with the Doctor class
            medications = sessions.create_medication_session()
            self.clear_screen()
            #print all of the medications if user wants to view all medications
            if options[menu_entry_index] == 'View all medications':
                print(green('LIST OF ALL MEDICATIONS: \n'))
                for med in medications.all():
                    print(med)
            #Allow the user to enter a specific name and look for that medications information
            elif options[menu_entry_index] == 'Search by name':
                #get the user input and validate the users input name for medication
                medication_filter_name = validate.search_by('Meication', Medication)
                if medication_filter_name != None:
                    print('\n')
                    print(green('Medications(s):'))
                    for meds in medication_filter_name:
                        print(meds)
                        print(green(f'List of clients on Medication- {meds.name}:'))
                        for client in meds.clients:
                            print(f'{client.clients.name}, ID: {client.clients.id}')
            #Allow the user to search a medications with there id number
            elif options[menu_entry_index] == 'Search by ID':
                medication_filter_id = validate.validate_id('Medication', Medication)
                if medication_filter_id != None:
                    print('\n')
                    print(green('List of medications: '))
                    print(medication_filter_id[0])
                    print(green('List of clients on Medication- '))
                    for client in medication_filter_id[0].clients:
                        print(f'{client.clients.name}, ID: {client.clients.id}')
            else:
                return_home = True
            input(yellow('Press any key When ready.'))
        self.home_screen()

    def handle_med_schedule_choice(self):
        return_home = False
        while return_home == False:
            self.clear_screen()
            art.tprint("MEDICINE-SCHEDULE")
            print('Choose an option: ')
            #display options for user to choose medication schedule
            options = ['Sign Off medication time slot', 'View medication schedule', 'Filter by time', 'Return to main screen']
            terminal_menu = TerminalMenu(options)
            menu_entry_index = terminal_menu.show()
            #create a session with the Doctor class
            medications = sessions.create_med_times_session()
            self.clear_screen()
            #display the entire medication schedule
            if options[menu_entry_index] == 'View medication schedule':
                print(green('MEDICATION SCHEDULE: '))
                for times in medications.all():
                    print(times)
            #filters and displays depending on name
            elif options[menu_entry_index] == 'Filter by time':
                print(yellow('What time slot would you want to view ( 16:00 = 04:00 apm): '))
                user_input = helpers.time_slots()
                med_times_filter = medications.filter(Med_times.time_slot == user_input)
                print(green(f'List of {user_input}:'))
                for times in med_times_filter:
                    print(times)
            #filters and displays a pecific time
            elif options[menu_entry_index] == 'Sign Off medication time slot':
                print(green('Enter the client information and the time slot you want to sign off.'))
                client_id = validate.validate_id('Client', Client)
                time_slot = helpers.time_slots()
                print(client_id[0].id)
                client_id_signoff = medications.filter(Med_times.client_id == client_id[0].id)
                sign_off_time = client_id_signoff.filter(Med_times.time_slot == time_slot) 
                print(sign_off_time[0])
                user_input = input(green('Is this correct? (Y/N): '))
                if user_input == 'y'or user_input =='Y' or user_input =='yes'or user_input == 'Yes':
                    sign_off_time[0].signed_off = self.current_user.id
                    sessions.session_create().commit()
                    print(yellow(str(sign_off_time[0]))) 
                    print(green('\thas been signed by you.')) 
                else:
                    print(red('SIGN OFF WAS NOT SUCCESSFUL'))
            else:
                return_home = True
            input(yellow('Press any key When ready.'))
        self.home_screen()
    
    def handle_modify_info(self): 
        return_home = False
        while return_home == False:
            self.clear_screen()
            art.tprint("MODIFY-TABLES'S")
            print('What would you like to do? ')
            modify_options = ['Remove', 'Add', 'Return to main window']
            modify_terminal_menu = TerminalMenu(modify_options)
            modify_menu_entry_index = modify_terminal_menu.show()

            if modify_options[modify_menu_entry_index] == 'Return to main window':
                return_home = True
            else:
                print(f'What information would you like to {modify_options[modify_menu_entry_index]}: ')
                options = ['Client', 'Medication Scheduling', 'Return to main window']
                terminal_menu = TerminalMenu(options)
                menu_entry_index = terminal_menu.show()

                if options[menu_entry_index] == 'Client':
                    if modify_options[modify_menu_entry_index] == 'Add':
                        modify.handle_add_client()
                    else:
                        modify.remove_client()
                elif options[menu_entry_index] == 'Medication Scheduling':
                    if modify_options[modify_menu_entry_index] == 'Add':
                        modify.handle_add_med_times(self.current_user.id)
                    else:
                        modify.remove_med_time()
                elif options[menu_entry_index] == 'Return to main window':
                    return_home = True 
            input(yellow('Press any key When ready.'))
        self.home_screen()

app = Cli()
app.start()