import re

def LogSquadTrace_Deployable_Damage(data_str, server_id):
    matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogSquadTrace: \[DedicatedServer]ASQDeployable::"
                         r"TakeDamage\(\): (.*): (\d+(\.\d+)?) damage taken by causer (.*) instigator (.*)"
                         r" health remaining (\d+(\.\d+)?)", data_str, re.M | re.I | re.S)
    temp_set = 0

    if matchObj == None:
        matchObj = re.search(r"[([0-9.:-]+]\[([ 0-9]*)]LogSquadTrace: \[DedicatedServer]ASQDeployable::"
                             r"TakeDamage\(\): (.*): (\d+(\.\d+)?) damage attempt by causer (.*) instigator (.*) with damage"
                             r" type (.*) health remaining (\d+(\.\d+)?)",
                             data_str, re.M | re.I | re.S)

        pass
    date = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[0]
    time = (matchObj.group(0).split("[")[1].split(']')[0]).split("-")[1]
    Damage_taker = matchObj.group(2)
    Damage = matchObj.group(3)
    By_Weapon = matchObj.group(5)
    By_Player = matchObj.group(6)
    if temp_set == 0:
        Damage_type = None
        Health_remain = matchObj.group(7)
        pass
    else:
        Damage_type = matchObj.group(7)
        Health_remain = matchObj.group(8)
        pass
    return (date, time, str(Damage_taker), float(Damage), str(By_Weapon), str(By_Player),
            str(Damage_type), str(Health_remain), server_id)
    pass

