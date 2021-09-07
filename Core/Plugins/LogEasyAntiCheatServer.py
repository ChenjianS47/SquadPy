import re

# Define a function for reading the player steam64id from the line LogEasyAntiCheatServer


def LogEasyAntiCheatServer(data_str):
    matchobj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogEasyAntiCheatServer: .*Client: (.*) PlayerGUID: (.*) "
                         r"PlayerIP: (.*) OwnerGUID: (.*) PlayerName: .", data_str, re.M | re.I)
    date = (matchobj.group(0).split("[")[1].split(']')[0]).split("-")[0]
    time = (matchobj.group(0).split("[")[1].split(']')[0]).split("-")[1]
    player_64id = matchobj.group(3)
    return (date, time, str(player_64id))
    pass
