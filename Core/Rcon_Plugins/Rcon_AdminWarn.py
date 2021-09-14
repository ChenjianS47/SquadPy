import Core.Base.Pyscrds_modified as rcon


def Rcon_AdminWarn(server_rcon_info, server_name, steam_64id, warning_info):
    conn = rcon.RconConnection(server=server_rcon_info[server_name]['Server_IP'],
                               port=server_rcon_info[server_name]['RCON_Port'],
                               password=server_rcon_info[server_name]['Server_pw'])
    warning = 'AdminWarn ' + steam_64id + ' ' + warning_info
    conn.exec_command(warning)
    pass
