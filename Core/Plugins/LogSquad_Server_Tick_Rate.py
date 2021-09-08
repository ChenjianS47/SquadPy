import re
import datetime


def LogSquad_Server_Tick_Rate(data_str, server_id):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogSquad: USQGameState: Server Tick Rate: (\d+(\.\d+)?)",
                         data_str, re.M | re.I)
    date_time = datetime.datetime.strptime(matchObj.group(0).split("[")[1].split(']')[0], "%Y.%m.%D-%H.%M.%S:%f")
    date_time_n = (date_time + datetime.timedelta(hours=8)).strftime("%Y.%m.%D-%H.%M.%S:%f")
    date = date_time_n.split("-")[0]
    time = date_time_n.split("-")[1]
    Server_Tick_Rate = matchObj.group(2)
    return (date, time, str(Server_Tick_Rate), server_id)
    pass
