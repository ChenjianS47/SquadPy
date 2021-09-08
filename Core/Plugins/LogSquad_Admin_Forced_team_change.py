import re
import datetime

def LogSquad_Admin_Forced_team_change(data_str, server_id):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogSquad: ADMIN COMMAND: Forced team change for (.*) from .*",
                         data_str, re.M | re.I)
    date_time = datetime.datetime.strptime(matchObj.group(0).split("[")[1].split(']')[0], "%Y.%m.%D-%H.%M.%S:%f")
    date_time_n = (date_time + datetime.timedelta(hours=8)).strftime("%Y.%m.%D-%H.%M.%S:%f")
    date = date_time_n.split("-")[0]
    time = date_time_n.split("-")[1]
    CMD = "Forced team change"
    Info = matchObj.group(2)
    return (date, time, CMD, str(Info), server_id)
    pass


