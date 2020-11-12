import json
import os
import pickle


def pickle_load():
    if os.path.getsize('phonebook.pickle') > 0:
        with open(f"phonebook.pickle", "rb") as f:
            pickled_data = pickle.load(f)
    return pickled_data


def pickle_save(phonebook):
    with open("phonebook.pickle", "wb") as f:
        pickle.dump(phonebook, f)
        print('Phonebook saved into phonebook.pickle')
    exit()


def json_load():
    if os.path.getsize('phonebook.json') > 0:
        with open(f"phonebook.json", "rb") as f:
            pickled_data = json.load(f)
    return pickled_data


def json_save(phonebook):
    with open("phonebook.json", "wt") as f:
        json.dump(phonebook, f)
        print('Phonebook saved into phonebook.json')
    exit()



