import re

def LogSquadTrace_Match_Winner(data_str, server_id):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogSquadTrace: \[DedicatedServer]ASQGameMode::"
                         r"?DetermineMatchWinner\(\): (.*) on (.*)", data_str, re.M | re.I | re.S)
    date = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[0]
    time = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[1]
    winner = matchObj.group(2)
    layer = matchObj.group(3)
    return (date, time, str(winner), str(layer), server_id)
    pass
