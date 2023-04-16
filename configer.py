from enum_keys import EnumKeys as ek
import configparser
import os

class Configer:
    config = configparser.ConfigParser()
    dir_path = 'configs'
    file_path = dir_path + '/config.ini'

    server_url = ''
    site_name = ''
    display_name = ''
    token_name = ''
    token_value = ''

    @classmethod
    def initialize(cls):
        cls.initialize_format()
        cls.load_auth()

    @classmethod
    def get_home_url(cls) -> str:
        home_url = cls.server_url
        if cls.site_name != '':
            home_url += '/#/site/' + cls.site_name

        return home_url

    @classmethod
    def initialize_format(cls):
        if not os.path.isdir(cls.dir_path):
            os.mkdir(cls.dir_path)

        if os.path.isfile(cls.file_path):
            cls.config.read(cls.file_path)
        else:
            cls.config.add_section('AUTH')
            cls.config.set('AUTH', 'server_url', '')
            cls.config.set('AUTH', 'site_name', '')
            cls.config.set('AUTH', 'display_name', '')
            cls.config.set('AUTH', 'token_name', '')
            cls.config.set('AUTH', 'token_value', '')

            with open(cls.file_path, 'w', encoding='utf-8') as f:
                cls.config.write(f)

    @classmethod
    def load_auth(cls):
        cls.server_url   = cls.config.get('AUTH', 'server_url')
        cls.site_name    = cls.config.get('AUTH', 'site_name')
        cls.display_name = cls.config.get('AUTH', 'display_name')
        cls.token_name   = cls.config.get('AUTH', 'token_name')
        cls.token_value  = cls.config.get('AUTH', 'token_value')

    @classmethod
    def save_auth(cls, values):
        cls.config.set('AUTH', 'server_url', values[ek.CONFIG_SERVER_URL_INPUT])
        cls.config.set('AUTH', 'site_name', values[ek.CONFIG_SITE_NAME_INPUT])
        cls.config.set('AUTH', 'display_name', values[ek.CONFIG_DISPLAY_NAME_INPUT])
        cls.config.set('AUTH', 'token_name', values[ek.CONFIG_TOKEN_NAME_INPUT])
        cls.config.set('AUTH', 'token_value', values[ek.CONFIG_TOKEN_VALUE_INPUT])

        with open(cls.file_path, 'w', encoding='utf-8') as f:
            cls.config.write(f)
        
        cls.load_auth()