import re


def LogSquadTrace_Vehicle_Damage(data_str, server_id):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogSquadTrace: \[DedicatedServer]ASQVehicleSeat::"
                         r"TraceAndMessageClient\(\): (.*): (\d+(\.\d+)?) damage taken by causer (.*)"
                         r" instigator (.*) health remaining (\d+(\.\d+)?)",
                         data_str, re.M | re.I | re.S)
    if str(matchObj) == "None":
        matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogSquadTrace: \[DedicatedServer]ASQVehicleSeat::"
                             r"TraceAndMessageClient\(\): (.*): (\d+(\.\d+)?) damage taken by causer (.*)"
                             r" instigator (.*) health remaining -(\d+(\.\d+)?)",
                             data_str, re.M | re.I | re.S)
        pass
    date = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[0]
    time = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[1]
    Destoryed_Vehichle = matchObj.group(2)
    Damage = matchObj.group(3)
    By_Weapon = matchObj.group(5)
    By_Player = matchObj.group(6)
    Health_remain = matchObj.group(7)
    return (date, time, str(Destoryed_Vehichle), float(Damage), str(By_Weapon), str(By_Player),
            str(Health_remain), server_id)
    pass