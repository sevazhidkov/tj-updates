import json

config_path = 'config.json'  # Path to config file
config_params = ['vk-login', 'vk-password']  # Params, which are saving to config file


def create_config():
    """Function makes a new config file"""
    new_config_file = open(config_path, 'w')
    config = {}
    for param in config_params:
        print('Enter value for "{}" parameter'.format(param))
        config.update({param: input()})
    new_config_file.write(json.dumps(config))
    new_config_file.close()
    return True


def open_config():
    """Function returns config file"""
    try:
        config_file = open(config_path)
    except FileNotFoundError:
        print('Config file is not found.')
        create_config()
        config_file = open(config_path)
    return config_file

config_file = open_config()
config = json.loads(config_file.read())

VK_LOGIN = config['vk-login']
VK_PASSWORD = config['vk-password']

config_file.close()