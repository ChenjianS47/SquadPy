import re
import datetime


def Rcon_Chat_AdminCamera(chat_msg, server_id):
    if re.search(r'\[SteamID:(.*)] (.*) has possessed admin camera.', chat_msg, re.M | re.S) is not None:
        matchOjb = re.search(r'\[SteamID:(.*)] (.*) has possessed admin camera.', chat_msg, re.M | re.S)
        date = datetime.datetime.now().strftime("%Y.%m.%d")
        time = datetime.datetime.now().strftime("%H.%M.%S:%f")
        Player_64id = matchOjb.group(1)
        Player_name = matchOjb.group(2)
        chat_content = 'Active AdminCamera'
        server_id = server_id
        return date, time, Player_64id, Player_name, chat_content, server_id
    elif re.search(r'\[SteamID:(.*)] (.*) has unpossessed admin camera.', chat_msg, re.M | re.S) is not None:
        matchOjb = re.search(r'\[SteamID:(.*)] (.*) has unpossessed admin camera.', chat_msg, re.M | re.S)
        date = datetime.datetime.now().strftime("%Y.%m.%d")
        time = datetime.datetime.now().strftime("%H.%M.%S:%f")
        Player_64id = matchOjb.group(1)
        Player_name = matchOjb.group(2)
        chat_content = 'Inactive AdminCamera'
        server_id = server_id
        return date, time, Player_64id, Player_name, chat_content, server_id
    pass

