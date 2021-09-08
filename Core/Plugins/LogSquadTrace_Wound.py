import re
import datetime

# Define a function for reading the wound data in the battle
def LogSquadTrace_Wound(data_str, server_id):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogSquadTrace: \[DedicatedServer](?:ASQSoldier::)?Wound\(\): "
                         r"Player:(.+) KillingDamage=(\d+(\.\d+)?) from (.*) caused by (.*)", data_str,
                         re.M | re.I | re.S)
    date_time = datetime.datetime.strptime(matchObj.group(0).split("[")[1].split(']')[0], "%Y.%m.%D-%H.%M.%S:%f")
    date_time_n = (date_time + datetime.timedelta(hours=8)).strftime("%Y.%m.%D-%H.%M.%S:%f")
    date = date_time_n.split("-")[0]
    time = date_time_n.split("-")[1]
    Player_Victim_name = matchObj.group(2)
    Damage = matchObj.group(3)
    Player_attcker_Controller = matchObj.group(5)
    Weapon = matchObj.group(6)
    return (date, time, str(Player_Victim_name), float(Damage), str(Player_attcker_Controller), str(Weapon), server_id)
    pass

