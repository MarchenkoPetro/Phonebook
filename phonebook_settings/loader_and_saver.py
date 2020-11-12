import csv
import json
import os
import pickle


def pickle_load():
    pickled_data = {}
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
    pickled_data = {}
    if os.path.getsize('phonebook.json') > 0:
        with open(f"phonebook.json", "rb") as f:
            pickled_data = json.load(f)

    return pickled_data


def json_save(phonebook):

    with open("phonebook.json", "wt") as f:
        json.dump(phonebook, f)
        print('Phonebook saved into phonebook.json')
    print('Phonebook saved into json format')
    exit()


def scv_load():
    pickled_data = {}
    if os.path.getsize('phonebook.csv') > 0:
        with open('phonebook.csv') as csv_file:
            reader = csv.reader(csv_file)
            pickled_data = dict(reader)
        print(pickled_data)
    return pickled_data


def scv_save(phonebook):
    with open('phonebook.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in phonebook.items():
            writer.writerow([key, value])
    print('Phonebook saved into scv format')
    exit()


