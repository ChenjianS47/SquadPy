
import re

# Define a function for reading the player name from the line Join succeeded and mark the end of player join


def LogNet_succed(data_str):
    global server_id
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogNet: Join succeeded:(.+)", data_str, re.M | re.I)
    date = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[0]
    time = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[1]
    Player_name = matchObj.group(2)
    LogNeT_join = 0
    return (date, time, str(Player_name), LogNeT_join)
    pass
