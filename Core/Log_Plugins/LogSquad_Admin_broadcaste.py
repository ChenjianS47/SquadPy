import re
import datetime
# Define a function for reading the usage of the admin command(still bug for the user of cmd)


def LogSquad_Admin_broadcaste(data_str, server_id):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogSquad: ADMIN COMMAND: Message broadcasted (.*) from .*", data_str,
                         re.M | re.I)
    date_time = datetime.datetime.strptime(matchObj.group(0).split("[")[1].split(']')[0], "%Y.%m.%d-%H.%M.%S:%f")
    date_time_n = (date_time + datetime.timedelta(hours=8)).strftime("%Y.%m.%d-%H.%M.%S:%f")
    date = date_time_n.split("-")[0]
    time = date_time_n.split("-")[1]
    CMD = "broadcaste"
    Info = matchObj.group(2)
    return (date, time, CMD, str(Info), server_id)
    pass

