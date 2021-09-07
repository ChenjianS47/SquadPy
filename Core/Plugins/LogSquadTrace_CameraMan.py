import re

# Define a function for reading the cameraman usage in the server
def LogSquadTrace_CameraMan(data_str, server_id):
    matchObj = re.search(
        r"[([0-9.:-]+]\[([ 0-9]*)]LogSquadTrace: \[DedicatedServer](?:ASQPlayerController::)?OnPossess\(\): "
        r"PC=(.*) Pawn=CameraMan.*",
        data_str, re.M | re.I | re.S)
    date = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[0]
    time = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[1]
    cameraman_id = matchObj.group(2)
    return (date, time, str(cameraman_id), server_id)
    pass
