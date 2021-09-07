import re


# Define a function for reading the wound data in the battle
def LogSquadTrace_OnPossess(data_str, server_id):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogSquadTrace: \[DedicatedServer]ASQPlayerController::"
                         r"OnPossess\(\): PC=(.*). Pawn=(.*) FullPath=.*", data_str, re.M | re.I | re.S)
    date = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[0]
    time = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[1]
    player_name = matchObj.group(2)
    player_equip = matchObj.group(3)
    return (date, time, str(player_name),str(player_equip), server_id)
    pass
