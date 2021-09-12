import re
import datetime


def Rcon_Chat_AdminKick(chat_msg, server_id):
    matchOjb = re.search(r'(.*) was kicked: (.*)', chat_msg, re.M | re.S)
    date = datetime.datetime.now().strftime("%Y.%m.%d")
    time = datetime.datetime.now().strftime("%H.%M.%S:%f")
    player_name = matchOjb.group(1)
    kick_reason = matchOjb.group(2)
    server_id = server_id
    return date, time, player_name, kick_reason,  server_id

