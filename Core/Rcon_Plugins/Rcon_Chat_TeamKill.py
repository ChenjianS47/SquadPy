import re
import datetime


def Rcon_Chat_TeamKill(chat_msg, server_id):
    matchOjb = re.search(r'\[ChatAdmin] ASQKillDeathRuleset : Player (.*)%s Team Killed Player (.*)',
                         chat_msg, re.M | re.S)
    date = datetime.datetime.now().strftime("%Y.%m.%d")
    time = datetime.datetime.now().strftime("%H.%M.%S:%f")
    Player_attacker = matchOjb.group(1)
    Player_victim = matchOjb.group(2)
    chat_content = 'TeamKill'
    server_id = server_id
    return date, time, Player_attacker, Player_victim, chat_content, server_id
