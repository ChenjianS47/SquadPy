import re
import datetime

# Define a function for reading the revive data in the battle
def LogSquad_revive(data_str, server_id):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogSquad: (.*) has revived (.*)", data_str, re.M | re.I)
    date_time = datetime.datetime.strptime(matchObj.group(0).split("[")[1].split(']')[0], "%Y.%m.%d-%H.%M.%S:%f")
    date_time_n = (date_time + datetime.timedelta(hours=8)).strftime("%Y.%m.%d-%H.%M.%S:%f")
    date = date_time_n.split("-")[0]
    time = date_time_n.split("-")[1]
    Player_Rescuer = matchObj.group(2)
    Player_Rescued = matchObj.group(3)
    return (date, time, str(Player_Rescuer), str(Player_Rescued), server_id)
    pass

