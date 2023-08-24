import sessions
from prettycli import red,yellow,green
import helpers

from  db.models import Doctor, Med_times, Client, Medication, Employee

def validate_id(search_object_name, object):
    valid = False
    while valid == False:
        user_input = check_if_integer(yellow(f'Enter {search_object_name} id: '))
        session = sessions.session_create()
        validate_id = session.query(object).filter(object.id == user_input)
        if validate_id.count() != 0:
            return validate_id
        else:
            print(red(f'There is no {search_object_name} with that id.'))
            valid_response = False
            while valid_response == False: 
                keep_search = input('Would you like to keep searching (Y/N): ')
                if keep_search == 'y'or keep_search == 'Y' or keep_search == 'yes' or keep_search == 'Yes':
                    print('\n')
                    valid_response = True
                elif keep_search == 'n'or keep_search == 'N' or keep_search == 'No' or keep_search == 'no':
                    print(green('Id search ended.'))
                    valid = True
                    valid_response = True
                else:
                    print(red('Please insert a valid response.'))

def check_if_integer(user_promp):
    good_input = False
    while good_input == False:
        num = input(yellow(user_promp))
        if num.isdigit():
                return int(num)
        else:
            print(red('Value must be a number.'))

def search_by(search_item, object):
    x = False
    while x == False:
        user_input = input(yellow(f'What is the {search_item} name: '))
        session = sessions.session_create()
        filter_name = session.query(object).filter(object.name == user_input)
        if filter_name.count() != 0:
            return filter_name
        else:
            print(red(f'There is no {search_item} with that name.'))

