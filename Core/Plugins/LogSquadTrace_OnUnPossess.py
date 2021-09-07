import re


def LogSquadTrace_OnUnPossess(data_str, server_id):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogSquadTrace: \[DedicatedServer](?:ASQPlayerController::)"
                         r"?OnUnPossess\(\): PC=(.*).*", data_str, re.M | re.I | re.S)
    date = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[0]
    time = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[1]
    player_name = matchObj.group(2)
    return (date, time, str(player_name), server_id)
    pass
