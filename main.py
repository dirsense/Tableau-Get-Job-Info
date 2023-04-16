from configer import Configer as cf
from enum_keys import EnumKeys as ek
from config_manager import ConfigManager
import main_funcs as mf
import PySimpleGUI as sg

sg.theme('DarkGrey8')

def main():
    cf.initialize()

    layout = [
        [sg.Image(filename='image/inazuma.png', pad=((5, 0), (5, 5))),
         sg.Text(cf.get_home_url(), key=ek.HEADER_SERVER_URL_TEXT, background_color='#000000', pad=((3, 5), (5, 5))),
         sg.Image(filename='image/account.png', pad=((6, 0), (5, 5))),
         sg.Text(cf.display_name, key=ek.HEADER_DISPLAY_NAME_TEXT, background_color='#000000', pad=((3, 5), (5, 5))),
         sg.Image(key=ek.HEADER_WHEEL_IMAGE, filename='image/wheel.png', enable_events=True, pad=((5, 5), (5, 3)))],

        [sg.Text('Job LUID', pad=((5, 5), (1, 1)))],
        [sg.InputText(key=ek.JOB_ID_INPUT, size=(35, 1))],
        [sg.Button('Get Job Info', key=ek.GET_JOB_INFO_BUTTON, pad=((5, 5), (8, 5)))],
        [sg.Multiline(key=ek.JOB_INFO_MULTILINE, size=(35, 10), no_scrollbar=True, expand_x=True)]
    ]

    window = sg.Window('Tableau Get Job Info', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        
        elif event == ek.HEADER_WHEEL_IMAGE:
            conf = ConfigManager(window)
            conf.running()
            del conf

        elif event == ek.GET_JOB_INFO_BUTTON:
            mf.get_job_info(window, values)

    window.close()

if __name__ == '__main__':
    main()