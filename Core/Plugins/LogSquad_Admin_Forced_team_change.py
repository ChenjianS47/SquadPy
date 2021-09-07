import re

def LogSquad_Admin_Forced_team_change(data_str, server_id):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogSquad: ADMIN COMMAND: Forced team change for (.*) from .*",
                         data_str, re.M | re.I)
    date = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[0]
    time = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[1]
    CMD = "Forced team change"
    Info = matchObj.group(2)
    return (date, time, CMD, str(Info), server_id)
    pass


