import re
import datetime
# Define a function for reading the steam_64id for disconnect player


def LogOnline_disconnect(data_str, server_id):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogOnline: STEAM: (.*) has been removed.", data_str, re.M | re.I)
    date_time = datetime.datetime.strptime(matchObj.group(0).split("[")[1].split(']')[0], "%Y.%m.%D-%H.%M.%S:%f")
    date_time_n = (date_time + datetime.timedelta(hours=8)).strftime("%Y.%m.%D-%H.%M.%S:%f")
    date = date_time_n.split("-")[0]
    time = date_time_n.split("-")[1]
    Player_64id = matchObj.group(2)
    return (date, time, str(Player_64id), server_id)
    pass

