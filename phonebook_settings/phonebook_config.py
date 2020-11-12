import configparser
import os

from model import check_answer

SETTINGS_PATH = 'settings.ini'



def set_config():
    if not os.path.exists(SETTINGS_PATH):
        config = configparser.ConfigParser()
        config.add_section("Settings")
        config.set("Settings", "file_format", "pickle")  # Enter format for saving data: json or pickle

        with open(SETTINGS_PATH, "w") as config_file:
            config.write(config_file)


def read_config(path):
    config = configparser.ConfigParser()
    config.read(path)
    return config


def switch_file_format(path, file_format, config):

    intention = input(f'Current file format is {file_format}.Do you want to switch it (json/pickle)? Y/N ')

    if check_answer(intention):
        if file_format == 'json':
            config.set("Settings", "file_format", "pickle")
            file_format = 'pickle'
            print(f'Setting changed. New file-format is Pickle')
        else:
            config.set("Settings", "file_format", "json")
            file_format = 'json'
            print(f'Setting changed. New file-format is Json')

        with open(path, "w") as config_file:
            config.write(config_file)
    return file_format