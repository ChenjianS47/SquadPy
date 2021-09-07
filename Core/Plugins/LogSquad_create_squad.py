import re

# Define a function for reading squad creating info
def LogSquad_create_squad(data_str, server_id):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogSquad: (.*) \(Steam ID: (.*)\) has created (.*) "
                         r"\(Squad Name: (.*)\) on (.*)", data_str, re.M | re.I)
    date = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[0]
    time = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[1]
    Player_name = matchObj.group(2)
    Player_64id = matchObj.group(3)
    Player_Squad_name = matchObj.group(4)
    Team_name = matchObj.group(5)
    return (date, time, str(Player_name), int(Player_64id), str(Player_Squad_name), str(Team_name), server_id)
    pass

