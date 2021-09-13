import Core.Base.Pyscrds_modified as rcon


def Rcon_ListPlayers(server_rcon_info, server_name):
    conn = rcon.RconConnection(server=server_rcon_info[server_name]['Server_IP'],
                               port=server_rcon_info[server_name]['RCON_Port'],
                               password=server_rcon_info[server_name]['Server_pw'])
    info = conn.exec_command('ListPlayers')
    return info
