import csv
import json
import os
import pickle


class Loader:
    def __init__(self, f):
        self.file_format = f

    def load(self):
        print(f'current file format is => {self.file_format}')
        if self.file_format == 'pickle':
            data_load = self.pickle_load()

        elif self.file_format == 'json':
            data_load = self.json_load()
        elif self.file_format == 'csv':
            data_load = self.csv_load()
        else:
            data_load = self.pickle_load()

        return data_load

    @staticmethod
    def pickle_load():
        pickled_data = {}
        if os.path.getsize('phonebook.pickle') > 0:
            with open(f"phonebook.pickle", "rb") as f:
                pickled_data = pickle.load(f)
        return pickled_data

    @staticmethod
    def json_load():
        pickled_data = {}
        if os.path.getsize('phonebook.json') > 0:
            with open(f"phonebook.json", "rb") as f:
                pickled_data = json.load(f)

        return pickled_data

    @staticmethod
    def csv_load():
        pickled_data = {}
        if os.path.getsize('phonebook.csv') > 0:
            with open('phonebook.csv') as csv_file:
                reader = csv.reader(csv_file)
                pickled_data = dict(reader)
            print(pickled_data)
        return pickled_data


class Saver:

    def __init__(self, phonebook, file_format):
        self.phonebook = phonebook
        self.file_format = file_format

    def save(self):
        print(f'current file format is => {self.file_format}')
        if self.file_format == 'pickle':
            data_load = self.pickle_save(self.phonebook)
        elif self.file_format == 'json':
            data_load = self.json_save(self.phonebook)
        elif self.file_format == 'csv':
            data_load = self.csv_save(self.phonebook)
        else:
            data_load = self.pickle_save(self.phonebook)
        return data_load

    @staticmethod
    def pickle_save(phonebook):
        with open("phonebook.pickle", "wb") as f:
            pickle.dump(phonebook, f)
            print('Phonebook saved into phonebook.pickle')
        exit()
        return True

    @staticmethod
    def json_save(phonebook):
        with open("phonebook.json", "wt") as f:
            json.dump(phonebook, f)
            print('Phonebook saved into phonebook.json')
        print('Phonebook saved into json format')
        exit()
        return True

    @staticmethod
    def csv_save(phonebook):
        with open('phonebook.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in phonebook.items():
                writer.writerow([key, value])
        print('Phonebook saved into scv format')
        exit()
        return True
