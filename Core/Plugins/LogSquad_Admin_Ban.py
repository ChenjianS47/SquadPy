import re

# Define a function for reading the usage of the admin command(still bug for the user of cmd)


def LogSquad_Admin_Ban(data_str, server_id):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogSquad: ADMIN COMMAND: .* Banned (.*) from .*", data_str,
                         re.M | re.I)
    date = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[0]
    time = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[1]
    CMD = "Ban"
    Info = matchObj.group(2)
    return (date, time, CMD, str(Info), server_id)
    pass


