import re
import datetime

def LogSquadTrace_Match_Winner(data_str, server_id):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogSquadTrace: \[DedicatedServer]ASQGameMode::"
                         r"?DetermineMatchWinner\(\): (.*) on (.*)", data_str, re.M | re.I | re.S)
    date_time = datetime.datetime.strptime(matchObj.group(0).split("[")[1].split(']')[0], "%Y.%m.%d-%H.%M.%S:%f")
    date_time_n = (date_time + datetime.timedelta(hours=8)).strftime("%Y.%m.%d-%H.%M.%S:%f")
    date = date_time_n.split("-")[0]
    time = date_time_n.split("-")[1]
    winner = matchObj.group(2)
    layer = matchObj.group(3)
    return (date, time, str(winner), str(layer), server_id)
    pass
