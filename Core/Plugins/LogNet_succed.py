import re
import datetime

# Define a function for reading the player name from the line Join succeeded and mark the end of player join


def LogNet_succed(data_str):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogNet: Join succeeded: (.+)", data_str, re.M | re.I)
    date_time = datetime.datetime.strptime(matchObj.group(0).split("[")[1].split(']')[0], "%Y.%m.%D-%H.%M.%S:%f")
    date_time_n = (date_time + datetime.timedelta(hours=8)).strftime("%Y.%m.%D-%H.%M.%S:%f")
    date = date_time_n.split("-")[0]
    time = date_time_n.split("-")[1]
    Player_name = matchObj.group(2)
    LogNeT_join = 0
    return (date, time, str(Player_name), LogNeT_join)
    pass
