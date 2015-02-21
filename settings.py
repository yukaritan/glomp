import configparser
config = configparser.ConfigParser()

path = 'settings.ini'
config.read(path)


def reload():
    config.read(path)


def get_setting(name):
    try:
        return config['DEFAULT'][name]
    except KeyError:
        return None


# import json
#
# settings = json.load(open('settings.json', 'r'))
#
#
# def reload():
#     global settings  # if we assign to settings, make sure we're doing it in the outer scope
#     settings = json.load(open('settings.json', 'r'))
#
#
# def get_setting(name):
#     if name in settings:
#         return settings[name]
#     return None
#
#
# if __name__ == '__main__':
#     # converts json to ini
#
#     import configparser
#     config = configparser.ConfigParser()
#     config['DEFAULT'] = settings
#
#     with open('settings.ini', 'w+') as configfile:
#         config.write(configfile)
