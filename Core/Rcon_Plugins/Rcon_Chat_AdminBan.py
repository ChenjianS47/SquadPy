import re
import datetime


def Rcon_Chat_AdminBan(chat_msg, server_id):
    matchOjb = re.search(r'"(.*) \[SteamID (.*)] Banned player (.*). \[steamid=(.*)] (.*) for interval (.*)"',
                         chat_msg, re.M | re.S)
    date = datetime.datetime.now().strftime("%Y.%m.%d")
    time = datetime.datetime.now().strftime("%H.%M.%S:%f")
    Admin_Name = matchOjb.group(1)
    Admin_Steam_64id = matchOjb.group(2)
    Banned_64id = matchOjb.group(4)
    Banned_name = matchOjb.group(5)
    Banned_interval = matchOjb.group(6)
    server_id = server_id
    return date, time, Admin_Name, Admin_Steam_64id, Banned_64id, Banned_name, Banned_interval, server_id
