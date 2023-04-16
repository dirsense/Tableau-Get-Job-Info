from configer import Configer as cf
from enum_keys import EnumKeys as ek
from TSC_utility import TscUtility as tu
import PySimpleGUI as sg

class ConfigManager:
    def __init__(self, header_window: sg.Window):
        self.header_window = header_window

        auth_frame = [sg.Frame(' 認証設定 ', size=(420, 200), layout=[
            [sg.Text('Sever URL', size=(9, 1), pad=((5, 5), (5, 3))), sg.InputText(cf.server_url, key=ek.CONFIG_SERVER_URL_INPUT, pad=((0, 5), (5, 3)))],
            [sg.Text('Site name', size=(9, 1)), sg.InputText(cf.site_name, key=ek.CONFIG_SITE_NAME_INPUT, pad=((0, 5), (3, 3)))],
            [sg.Text('表示名', size=(9, 1)), sg.InputText(cf.display_name, key=ek.CONFIG_DISPLAY_NAME_INPUT, pad=((0, 5), (3, 3)))],
            [sg.Text('トークン名', size=(9, 1)), sg.InputText(cf.token_name, key=ek.CONFIG_TOKEN_NAME_INPUT, pad=((0, 5), (3, 3)))],
            [sg.Text('トークン値', size=(9, 1)), sg.InputText(cf.token_value, key=ek.CONFIG_TOKEN_VALUE_INPUT, password_char='*', pad=((0, 5), (3, 3)))],
            [sg.Button('認証テスト', key=ek.CONFIG_AUTH_TEST_BUTTON, button_color=('#bbbc6c', '#11181f'), size=(39, 1), pad=((48, 5), (12, 3)))],
        ])]

        self.layout = [
            [auth_frame],
            [sg.Button('設定を保存', key=ek.CONFIG_SAVE_BUTTON, size=(39, 1), pad=((55, 5), (8, 4)))],
        ]

        self.window = sg.Window('Auth Settings', layout=self.layout, modal=True)
    
    def running(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                break

            elif event == ek.CONFIG_AUTH_TEST_BUTTON:
                if tu.login(values[ek.CONFIG_TOKEN_NAME_INPUT], values[ek.CONFIG_TOKEN_VALUE_INPUT],
                            values[ek.CONFIG_SERVER_URL_INPUT], values[ek.CONFIG_SITE_NAME_INPUT]):
                    sg.popup('認証に成功しました', no_titlebar=True, background_color='#4a6886')

            elif event == ek.CONFIG_SAVE_BUTTON:
                cf.save_auth(values)
                self.header_window[ek.HEADER_SERVER_URL_TEXT].update(cf.get_home_url())
                self.header_window[ek.HEADER_DISPLAY_NAME_TEXT].update(cf.display_name)
                sg.popup('設定の保存が完了しました', no_titlebar=True, background_color='#4a6886')
        
        self.window.close()
