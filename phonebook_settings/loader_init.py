from phonebook_settings.phonebook_config import read_config, SETTINGS_PATH

config = read_config(SETTINGS_PATH)
file_format = config['Settings']['file_format']

def switch_file_format():
    global file_format
    print(file_format)
    answer = input(f'Current file format is {file_format}.Enter new file_format (json/pickle/csv)?')

    if answer == 'pickle':
        config.set("Settings", "file_format", "pickle")
        file_format = 'pickle'
        print(f'Setting changed. New file-format is Pickle')
    elif answer == 'json':
        config.set("Settings", "file_format", "json")
        file_format = 'json'
        print(f'Setting changed. New file-format is json')
    elif answer == 'scv':
        config.set("Settings", "file_format", "scv")
        file_format = 'scv'
        print(f'Setting changed. New file-format is scv')
    else:
        config.set("Settings", "file_format", "scv")
        file_format = 'scv'
        print(f'Default file-format is set  =>  scv')

    with open(SETTINGS_PATH, "w") as config_file:
        config.write(config_file)

    return file_format


def load():
    print(f'current file format is => {file_format}')
    if file_format == 'pickle':
        from phonebook_settings.loader_and_saver import pickle_load as data_load
    elif file_format == 'json':
        from phonebook_settings.loader_and_saver import json_load as data_load
    elif file_format == 'csv':
        from phonebook_settings.loader_and_saver import scv_load as data_load
    else:
        from phonebook_settings.loader_and_saver import pickle_load as data_load

    return data_load()


def save(phonebook):
    global file_format

    if file_format == 'pickle':
        from phonebook_settings.loader_and_saver import pickle_save as data_save
    if file_format == 'json':
        from phonebook_settings.loader_and_saver import json_save as data_save
    if file_format == 'scv':
        from phonebook_settings.loader_and_saver import scv_save as data_save

    return data_save(phonebook)


