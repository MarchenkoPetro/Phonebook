from phonebook_settings.phonebook_config import read_config, SETTINGS_PATH

config = read_config(SETTINGS_PATH)
file_format = config['Settings']['file_format']

def switch_file_format():
    global file_format
    answer = input(f'Current file format is {file_format}.Do you want to switch it (json/pickle)? Y/N ')

    if file_format == 'json':
        config.set("Settings", "file_format", "pickle")
        file_format = 'pickle'
        print(f'Setting changed. New file-format is Pickle')
    else:
        config.set("Settings", "file_format", "json")
        file_format = 'json'
        print(f'Setting changed. New file-format is Json')

    with open(SETTINGS_PATH, "w") as config_file:
        config.write(config_file)

    return file_format


def load():

    if file_format == 'pickle':
        from phonebook_settings.loader_and_saver import pickle_load as data_load
    if file_format == 'json':
        from phonebook_settings.loader_and_saver import json_load as data_load
    return data_load()


def save(phonebook):
    global file_format

    if file_format == 'pickle':
        from phonebook_settings.loader_and_saver import pickle_save as data_save
    if file_format == 'json':
        from phonebook_settings.loader_and_saver import json_save as data_save
    return data_save(phonebook)


