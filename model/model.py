import json
import os
import pickle

from view import check_answer


def read_phonebook(file_format):
    """
    Open phonebook and upload it into Memory
    Returns object Phonebook = {}
    """

    pickled_data = {}
    if file_format == 'pickle':
        if os.path.getsize('phonebook.pickle') > 0:
            with open(f"phonebook.pickle", "rb") as f:
                pickled_data = pickle.load(f)

    elif os.path.getsize('phonebook.json') > 0:
        with open(f"phonebook.json", "rb") as f:
            pickled_data = json.load(f)
    return pickled_data


def create_new_contact(phonebook, name):
    """
    CREATE new contact if phonebook doesn't include it. Otherwise - update contact
    """

    if name in phonebook:
        print('There is already such a contact. Do you want to change its number?')
        answer = input('Enter Y or N: ').strip().lower()
        if check_answer.check_answer(answer):
            update_contact(phonebook, name)
    else:
        phone_number = input('Enter a number for this contact:')
        enter_number_into_contact(phonebook, name, phone_number)

    return


def update_contact(phonebook, name):
    """UPDATE contact"""
    if name not in phonebook:
        print('There is no such a contact')
        return
    phone_number = input('Enter new number for this contact:')
    enter_number_into_contact(phonebook, name, phone_number)


def delete_contact(phonebook, contact_name):
    """DELETE the contact"""
    if contact_name in phonebook:
        del phonebook[contact_name]
        print(f'You deleted the contact: {contact_name}')
    else:
        print('There is no such a contact')


def enter_number_into_contact(phonebook, contact_name, phone_number):
    """
    Validate phone - must be only digits
    Enter validated phone into contact
    """

    try:
        validated_phone = int(phone_number)
    except ValueError:
        print('You can put digits as phone number')
    else:
        phonebook[contact_name] = validated_phone
        print(f'Name: {contact_name},  phone number: {phonebook[contact_name]}')


def save_phonebook_and_exit(phonebook, file_format):
    if file_format == 'pickle':
        with open("phonebook.pickle", "wb") as f:
            pickle.dump(phonebook, f)
            print('Phonebook saved into phonebook.pickle')
    elif file_format == 'json':
        with open("phonebook.json", "wt") as f:
            json.dump(phonebook, f)
            print('Phonebook saved into phonebook.json')

    else:
        raise ValueError('Can not save your changes. Format for saving data is neither json or pickle')
    exit()


def print_help_list():
    """
    SHOW user all available commands
    """
    print('''There is a list of available operations:
    A  - to see all the contacts in phonebook
    F - to find a contact using its name
    C - to create a contact
    U - to update some contact
    D - to delete some contact 
    S - enter to setting menu
    ''')
