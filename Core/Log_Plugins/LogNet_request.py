import re
import datetime
# Define a function for reading the player name from the line LogNet: Join request and mark the start of player join


def LogNet_request(data_str):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogNet: Join request: "
                         r"/Game/Maps/EntryMap.*Name=(.+).*SplitscreenCount=1", data_str, re.M | re.I)
    date_time = datetime.datetime.strptime(matchObj.group(0).split("[")[1].split(']')[0], "%Y.%m.%d-%H.%M.%S:%f")
    date_time_n = (date_time + datetime.timedelta(hours=8)).strftime("%Y.%m.%d-%H.%M.%S:%f")
    date = date_time_n.split("-")[0]
    time = date_time_n.split("-")[1]
    Player_name = (matchObj.group(2))[:-1]
    LogNeT_join = 1
    return (date, time, str(Player_name), LogNeT_join)
    pass
