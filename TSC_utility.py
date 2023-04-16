from configer import Configer as cf
import PySimpleGUI as sg
import tableauserverclient as TSC

class TscUtility:
    server = None
    request_options = TSC.RequestOptions(pagesize=1000)

    @classmethod
    def login(cls, token_name=None, token_value=None, server_url=None, site_name=None) -> bool:
        token_name  = cf.token_name  if token_name  is None else token_name
        token_value = cf.token_value if token_value is None else token_value
        server_url  = cf.server_url  if server_url  is None else server_url
        site_name   = cf.site_name   if site_name   is None else site_name

        try:
            tableau_auth = TSC.PersonalAccessTokenAuth(token_name, token_value, site_name)
            cls.server = TSC.Server(server_url, use_server_version=True)
            cls.server.auth.sign_in(tableau_auth)

        except Exception as e:
            msg = 'サーバーログイン処理でエラーが発生しました\n' + str(e) + '\n\n'\
                + '※トークン名またはトークン値が正しいか確認して下さい\n'\
                + '※トークンは１５日間連続でログインが無いと無効になります（有効期間最長：１年）\n'\
                + '※トークンが無効になった場合はトークンを再発行＆再設定して下さい\n'
            sg.popup(msg, title='Login Error')
            return False
        else:
            return True