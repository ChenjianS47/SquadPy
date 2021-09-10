import Core.Plugins.rcon_pyscrds as rcon
from config import server_rcon


def rcon_cmd(threadID):
    rcon.RconConnection(server=server_rcon[threadID]['Server_IP'],port=server_rcon[threadID]['RCON_Port'],
                        password=server_rcon[threadID]['Server_pw'])

    pass
