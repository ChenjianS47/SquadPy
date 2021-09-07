import re


# Define a function for reading the Controller number of the player
def LogSquad_PostLogin(data_str):
    matchObj = re.search(
        r"[([0-9.:-]+]\[([ 0-9]*)]LogSquad: PostLogin: NewPlayer: BP_PlayerController_C.*PersistentLevel.(.+)"
        , data_str, re.M | re.I)
    date = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[0]
    time = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[1]
    Player_controller = matchObj.group(2)
    return (date, time, str(Player_controller))
    pass


