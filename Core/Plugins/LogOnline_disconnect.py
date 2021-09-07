import re

# Define a function for reading the steam_64id for disconnect player


def LogOnline_disconnect(data_str, server_id):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogOnline: STEAM: (.*) has been removed.", data_str, re.M | re.I)
    date = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[0]
    time = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[1]
    Player_64id = matchObj.group(2)
    return (date, time, str(Player_64id), server_id)
    pass

