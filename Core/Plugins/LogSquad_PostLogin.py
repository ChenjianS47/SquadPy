import re
import datetime


# Define a function for reading the Controller number of the player
def LogSquad_PostLogin(data_str):
    matchObj = re.search(
        r"[([0-9.:-]+]\[([ 0-9]*)]LogSquad: PostLogin: NewPlayer: BP_PlayerController_C.*PersistentLevel.(.+)[\s]"
        , data_str, re.M | re.I)
    date_time = datetime.datetime.strptime(matchObj.group(0).split("[")[1].split(']')[0], "%Y.%m.%D-%H.%M.%S:%f")
    date_time_n = (date_time + datetime.timedelta(hours=8)).strftime("%Y.%m.%D-%H.%M.%S:%f")
    date = date_time_n.split("-")[0]
    time = date_time_n.split("-")[1]
    Player_controller = (matchObj.group(2))[:-1]
    return (date, time, str(Player_controller))
    pass


