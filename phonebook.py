from phonebook_settings.phonebook_config import SETTINGS_PATH, set_config, read_config, switch_file_format
from model.model import create_new_contact, update_contact, delete_contact, save_phonebook_and_exit, print_help_list, \
    read_phonebook
print('test git connection')
set_config()
config = read_config(SETTINGS_PATH)
file_format = config['Settings']['file_format']
phonebook = read_phonebook(file_format)

while True:
    command = input('enter a key for operation (or enter \'help\') : ').strip().lower()

    if command == 'help':
        print_help_list()

    elif command == 'a':
        if not phonebook:
            print('Your phonebook is empty.')
            continue
        print('Your phonebook:')
        for name, number in phonebook.items():
            print(f'{name} : {number}')

    elif command == 'f':
        name = input('Enter a name you want to check:').capitalize()
        if name in phonebook:
            print(f'Detailed information: {name} : {phonebook[name]}')
        else:
            print('There is no such a contact')

    elif command == 'c':
        name = input('Enter name for new contact: \n').capitalize()
        create_new_contact(phonebook, name)

    elif command == 'u':
        name = input('Enter a name you want to update:').capitalize()
        update_contact(phonebook, name)

    elif command == 'd':
        name = input('Enter a name you want to delete from your phonebook:') \
            .capitalize()
        delete_contact(phonebook, name)

    elif command == 's':
        file_format = switch_file_format(SETTINGS_PATH, file_format, config)

    elif command == 'q':
        save_phonebook_and_exit(phonebook, file_format)

    else:
        print('There is no such a command. Try again')
