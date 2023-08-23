# Doctor Kevin House
- Please run pipenv shell
- cd into the lib directory
- run Python seed_2.py
- once finshed run Python cli.py to start the program

## Project requirements

In this project, we're going to use these skills to create a CLI. You won't be able to fit everything in from phase 3, but the following are the minimum requirements:
- A CLI application that solves a real-world problem and adheres to best practices.
- A database created and modified with SQLAlchemy ORM with 2+ related tables.
- A well-maintained virtual environment using Pipenv.
- Proper package structure in your application.
- Use of lists and dicts

Consider these stretch goals as you progress through your project:

- database created and modified with SQLAlchemy ORM with 3+ related tables.
- Use of many-to-many relationships with SQLAlchemy ORM.
- Use of additional data structures, such as ranges and tuples.

## Creating project
To start the project I used the template provided by the course for phase 3 project. I then removed the metadata as instructed using rm -rf .git .canvas
This removed the Git Repo and allows me to create and track my own local repository and push it into my own Git Repo. I renamed the file to project name, the used git init
to create my local repository. git add --all then added all the local files. git commit -m'initial commit' made my first commit and commit al my saved work to the repository. I creatyed a new reposiroty on my GitHub website. I copied the shh and ran git remote add origin `<github url>` to map my local repository to my git hub repo. Finally i pushed using git push -u origin main to make my first push and upload my project to my github repo.

## Installing necessary libraries and packages
For this project i install sqlalchemy and alembic to start. 

    pipenv install sqlalchemy alembic
installed the sqlalchemy library anlong with the alembic library. Then I was ready to enter my pip enviroment. 

    pipenv shell
## Functionality
### This project runs on SQLAlchemy and many packages. The version of python used is 3.8

### Terminal loads 

The terminal displays a message of my project name, _DOCTOR-KEVIN_HOUSE_, and a small greting. The user is prompted to select one of two choices, either Login or Exit. Exit will end the program. If the user selects Login it will take the user to the EMPLOYEE-LOGIN where the user is prompted to enter an email to login into there personal acount with there employee ID as the current user. Once an accepted email has been inputed the user will be directed to the home screen. 

### Home 
A greeting will be displayed showing the current users name. A few options will be displayed allowing the user to choose one of the options and continue with tye program as they need. 
![Alt text](image.png)

### def handle_client_Choice(self)
If the user selcts the clients option they will directed to the method handle_client_choice. A while loop is used to keep the user inside the client choice for as long as the wish to be, in can be broken when the return_home variable is set to True. A message is printed to choose an option 
            
    options = [
        'View all clients', 
        'Search by name', 
        'Search by ID', 
        'Return to main screen'
    ]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
A method from the sessions.py file is called, create_client_session, that has created a Client session. 
If the user selects _View all clients_, a list of clients will appear on the terminal. These are all the clients available in the client table. This is done by running a for loop and going threw all the instances stored in the client class. 

    if options[menu_entry_index] == 'View all clients':
        print(green('LIST OF ALL CLIENTS:'))
        for client in clients.all():
            print(client)
Once the user is satisfied with the viewing of the data they are prompted to press any key to return to the top of the loop and asked to choose another option in the client class. 
If the use chooses _Search by name_, the user is then promted to eneter a clients name. The program will use a method .filter() to filter all the instances in the clients table and see if there is a client with that name. If a name is found the clients information will print along with their medication time slots. The medication time slots are posiible because of a one-to-many relationship estabblished between the client and the med_times classes. 

    for client in client_filter_name:
        print(client)
        print(green(f'Medications perscribed: '))
        for meds in client.medications:
            print(meds.medications.name)
        print(green(f'Medication schedule for {client.name}'))
        for times in client.medications:
            print(times)