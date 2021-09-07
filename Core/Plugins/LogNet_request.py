import re

# Define a function for reading the player name from the line LogNet: Join request and mark the start of player join


def LogNet_request(data_str):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogNet: Join request: "
                         r"/Game/Maps/EntryMap.*Name=(.+).*SplitscreenCount=1", data_str, re.M | re.I)
    date = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[0]
    time = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[1]
    Player_name = matchObj.group(2)[:-1]
    LogNeT_join = 1
    return (date, time, str(Player_name), LogNeT_join)
    pass
