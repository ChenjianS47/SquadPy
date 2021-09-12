import re
import datetime


def Rcon_Chat_AdminDisbandSquad(chat_msg, server_id):
    matchOjb = re.search(r'Remote admin disbanded squad (.*) on team (.*), named "(.*)"',
                         chat_msg, re.M | re.S)
    date = datetime.datetime.now().strftime("%Y.%m.%d")
    time = datetime.datetime.now().strftime("%H.%M.%S:%f")
    squad_num = matchOjb.group(1)
    team = matchOjb.group(2)
    squad_name = matchOjb.group(3)
    server_id = server_id
    return date, time, squad_num, team, squad_name, server_id
