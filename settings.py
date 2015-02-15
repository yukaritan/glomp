import json

settings = json.load(open('settings.json', 'r'))


def reload():
    global settings  # if we assign to settings, make sure we're doing it in the outer scope
    settings = json.load(open('settings.json', 'r'))


def get_setting(name):
    if name in settings:
        return settings[name]
    return None