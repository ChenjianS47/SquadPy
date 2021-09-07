import re

def LogSquad_Damage(data_str, server_id):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogSquad: Player:(.*) ActualDamage=(\d+(\.\d+)?) from (.*) "
                         r"caused by (.*).*",
                         data_str, re.M | re.I)
    date = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[0]
    time = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[1]
    Player_take_damage = matchObj.group(2)
    Damage = matchObj.group(3)
    Player_make_damage = matchObj.group(5)
    Weapon = matchObj.group(6)
    return (date, time, str(Player_take_damage), str(Damage), str(Player_make_damage), str(Weapon), server_id)
    pass
