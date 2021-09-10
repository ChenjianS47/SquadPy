import Core.Plugins.pyscrds_modified as rcon
from config import server_rcon


def rcon_cmd_map_info(threadID):
    server_name = list(server_rcon.keys())[threadID]
    conn = rcon.RconConnection(server=server_rcon[server_name]['Server_IP'],port=server_rcon[server_name]['RCON_Port'],
                               password=server_rcon[server_name]['Server_pw'])
    cmd = conn.exec_command('ShowNextMap')
    info = conn.receive_chat_message()
    return info,cmd
    pass
while 1:
    print('s')
    print(rcon_cmd_map_info(0))
