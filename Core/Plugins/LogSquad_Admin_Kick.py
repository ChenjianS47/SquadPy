import re


def LogSquad_Admin_Kick(data_str, server_id):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogSquad: ADMIN COMMAND: Kicked (.*) from .*", data_str, re.M | re.I)
    date = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[0]
    time = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[1]
    CMD = "Kick"
    Info = matchObj.group(2)
    return (date, time, CMD, str(Info), server_id)
    pass

