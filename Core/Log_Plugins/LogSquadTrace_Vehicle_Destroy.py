import re
import datetime

def LogSquadTrace_Vehicle_Destroy(data_str, server_id):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogSquadTrace: \[DedicatedServer]ASQDestroyedVehicle::"
                         r"TakeDamage\(\): (.*): (\d+(\.\d+)?) damage taken by causer (.*) instigator (.*)"
                         r" health remaining (.*)",
                         data_str, re.M | re.I | re.S)
    temp_set = 0
    if matchObj == None:
        matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogSquadTrace: \[DedicatedServer]ASQDestroyedVehicle::"
                             r"TakeDamage\(\): (.*): (\d+(\.\d+)?) damage attempt by causer (.*) instigator (.*) with damage"
                             r" type (.*) health remaining (\d+(\.\d+)?).*",
                             data_str, re.M | re.I | re.S)
        temp_set = 1
        pass
    date_time = datetime.datetime.strptime(matchObj.group(0).split("[")[1].split(']')[0], "%Y.%m.%d-%H.%M.%S:%f")
    date_time_n = (date_time + datetime.timedelta(hours=8)).strftime("%Y.%m.%d-%H.%M.%S:%f")
    date = date_time_n.split("-")[0]
    time = date_time_n.split("-")[1]
    Destoryed_Vehichle = matchObj.group(2)
    Damage = matchObj.group(3)
    By_Weapon = matchObj.group(5).split("_C_")[0]
    By_Player = matchObj.group(6)
    if temp_set == 0:
        Damage_type = None
        Health_remain = matchObj.group(7)
        pass
    else:
        Damage_type = matchObj.group(7)
        Health_remain = matchObj.group(8)
        pass
    return (date, time, str(Destoryed_Vehichle), float(Damage), str(By_Weapon), str(By_Player),
            str(Damage_type), str(Health_remain), server_id)
    pass

