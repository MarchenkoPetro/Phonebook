from model.model import Phonebook
from phonebook_settings.loader_and_saver import Saver
from phonebook_settings.loader_init import switch_file_format, file_format
from phonebook_settings.phonebook_config import set_config


set_config()
new_phonebook = Phonebook()
phonebook = new_phonebook.phonebook

while True:
    command = input('enter a key for operation (or enter \'help\') : ').strip().lower()

    if command == 'help':
        new_phonebook.print_help_list()

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
        new_phonebook.create_new_contact(phonebook, name)

    elif command == 'u':
        name = input('Enter a name you want to update:').capitalize()
        new_phonebook.update_contact(phonebook, name)

    elif command == 'd':
        name = input('Enter a name you want to delete from your phonebook:') \
            .capitalize()
        new_phonebook.delete_contact(phonebook, name)

    elif command == 's':
        file_format = switch_file_format()

    elif command == 'q':
        saver = Saver(phonebook, file_format)
        saver.save()

    else:
        print('There is no such a command. Try again')
