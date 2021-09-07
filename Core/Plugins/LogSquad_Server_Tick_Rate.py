import re

def LogSquad_Server_Tick_Rate(data_str, server_id):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogSquad: USQGameState: Server Tick Rate: (\d+(\.\d+)?)",
                         data_str, re.M | re.I)
    date = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[0]
    time = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[1]
    Server_Tick_Rate = matchObj.group(2)
    return (date, time, str(Server_Tick_Rate), server_id)
    pass
