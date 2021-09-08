import re
import datetime

# Define a function for reading the wound data in the battle
def LogSquadTrace_OnPossess(data_str, server_id):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogSquadTrace: \[DedicatedServer]ASQPlayerController::"
                         r"OnPossess\(\): PC=(.*). Pawn=(.*) FullPath=.*", data_str, re.M | re.I | re.S)
    date_time = datetime.datetime.strptime(matchObj.group(0).split("[")[1].split(']')[0], "%Y.%m.%D-%H.%M.%S:%f")
    date_time_n = (date_time + datetime.timedelta(hours=8)).strftime("%Y.%m.%D-%H.%M.%S:%f")
    date = date_time_n.split("-")[0]
    time = date_time_n.split("-")[1]
    player_name = matchObj.group(2)
    player_equip = matchObj.group(3)
    return (date, time, str(player_name),str(player_equip), server_id)
    pass
