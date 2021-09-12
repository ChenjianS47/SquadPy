import re
import datetime


def Rcon_Chat_Chat(chat_msg, server_id):
    matchOjb = re.search(r'\[(.*)] \[SteamID:(.*)] (.*) : (.*)', chat_msg, re.M | re.I)
    date = datetime.datetime.now().strftime("%Y.%m.%d")
    time = datetime.datetime.now().strftime("%H.%M.%S:%f")
    chat_type = matchOjb.group(1)
    player_64id = matchOjb.group(2)
    player_name = matchOjb.group(3)
    chat_content = matchOjb.group(4)
    server_id = server_id
    return date, time, chat_type, player_64id, player_name, chat_content, server_id



