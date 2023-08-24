from prettycli import red, yellow
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

def terminal_choice(options):
    print('Choose an option: ')
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    return options[menu_entry_index]