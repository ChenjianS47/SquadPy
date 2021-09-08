import re
import datetime
# Define a function for reading the player steam64id from the line LogEasyAntiCheatServer


def LogEasyAntiCheatServer(data_str):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogEasyAntiCheatServer: .*Client: (.*) PlayerGUID: (.*) "
                         r"PlayerIP: (.*) OwnerGUID: (.*) PlayerName: .", data_str, re.M | re.I)
    date_time = datetime.datetime.strptime(matchObj.group(0).split("[")[1].split(']')[0], "%Y.%m.%d-%H.%M.%S:%f")
    date_time_n = (date_time + datetime.timedelta(hours=8)).strftime("%Y.%m.%d-%H.%M.%S:%f")
    date = date_time_n.split("-")[0]
    time = date_time_n.split("-")[1]
    player_64id = matchObj.group(3)
    return (date, time, str(player_64id))
    pass
