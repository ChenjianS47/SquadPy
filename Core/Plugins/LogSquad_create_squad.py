import re
import datetime

# Define a function for reading squad creating info
def LogSquad_create_squad(data_str, server_id):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogSquad: (.*) \(Steam ID: (.*)\) has created (.*) "
                         r"\(Squad Name: (.*)\) on (.*)", data_str, re.M | re.I)
    date_time = datetime.datetime.strptime(matchObj.group(0).split("[")[1].split(']')[0], "%Y.%m.%D-%H.%M.%S:%f")
    date_time_n = (date_time + datetime.timedelta(hours=8)).strftime("%Y.%m.%D-%H.%M.%S:%f")
    date = date_time_n.split("-")[0]
    time = date_time_n.split("-")[1]
    Player_name = matchObj.group(2)
    Player_64id = matchObj.group(3)
    Squad_sequnce_num = matchObj.group(4)
    Player_Squad_name = matchObj.group(5)
    Team_name = matchObj.group(6)
    return (date, time, str(Player_name), int(Player_64id), str(Squad_sequnce_num),
            str(Player_Squad_name), str(Team_name), server_id)
    pass

