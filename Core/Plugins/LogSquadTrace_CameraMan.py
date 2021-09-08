import re
import datetime

# Define a function for reading the cameraman usage in the server
def LogSquadTrace_CameraMan(data_str, server_id):
    matchObj = re.search(
        r"[([0-9.:-]+]\[([ 0-9]*)]LogSquadTrace: \[DedicatedServer](?:ASQPlayerController::)?OnPossess\(\): "
        r"PC=(.*) Pawn=CameraMan.*",
        data_str, re.M | re.I | re.S)
    date_time = datetime.datetime.strptime(matchObj.group(0).split("[")[1].split(']')[0], "%Y.%m.%D-%H.%M.%S:%f")
    date_time_n = (date_time + datetime.timedelta(hours=8)).strftime("%Y.%m.%D-%H.%M.%S:%f")
    date = date_time_n.split("-")[0]
    time = date_time_n.split("-")[1]
    cameraman_id = matchObj.group(2)
    return (date, time, str(cameraman_id), server_id)
    pass
