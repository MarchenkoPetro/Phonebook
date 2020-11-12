import configparser
import os

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


