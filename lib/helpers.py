from prettycli import red, green, yellow
from simple_term_menu import TerminalMenu

def time_slots():
    print(yellow('Choose time slot: '))
    options = []
    for i in range(4, 25, 4):
        options.append(f'{str(i)}:00')
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(options[menu_entry_index])
    return(options[menu_entry_index])

def check_if_integer(user_promp):
    num = input(yellow(user_promp))
    if num.isdigit():
            return int(num)
    else:
        print(red('Value must be a number.'))
        check_if_integer()