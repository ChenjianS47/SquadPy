import time as t_ime

from Core.Plugins.Insert_SQL import Insert_SQL
from Core.Plugins.read_logs import read_logs
from Core.Plugins.LogEasyAntiCheatServer import LogEasyAntiCheatServer
from Core.Plugins.LogNet_request import LogNet_request
from Core.Plugins.LogNet_succed import LogNet_succed
from Core.Plugins.LogOnline_disconnect import LogOnline_disconnect
from Core.Plugins.LogSquad_Admin_Ban import LogSquad_Admin_Ban
from Core.Plugins.LogSquad_Admin_broadcaste import LogSquad_Admin_broadcaste
from Core.Plugins.LogSquad_Admin_change_layer import LogSquad_Admin_change_layer
from Core.Plugins.LogSquad_Admin_disband_squad import LogSquad_Admin_disband_squad
from Core.Plugins.LogSquad_Admin_Forced_team_change import LogSquad_Admin_Forced_team_change
from Core.Plugins.LogSquad_Admin_Kick import LogSquad_Admin_Kick
from Core.Plugins.LogSquad_Admin_set_layer import LogSquad_Admin_set_layer
from Core.Plugins.LogSquad_create_squad import LogSquad_create_squad
from Core.Plugins.LogSquad_Damage import LogSquad_Damage
from Core.Plugins.LogSquad_map import LogSquad_map
from Core.Plugins.LogSquad_PostLogin import LogSquad_PostLogin
from Core.Plugins.LogSquad_revive import LogSquad_revive
from Core.Plugins.LogSquad_Server_Tick_Rate import LogSquad_Server_Tick_Rate
from Core.Plugins.LogSquadTrace_CameraMan import LogSquadTrace_CameraMan
from Core.Plugins.LogSquadTrace_Deployable_Damage import LogSquadTrace_Deployable_Damage
from Core.Plugins.LogSquadTrace_Die import LogSquadTrace_Die
from Core.Plugins.LogSquadTrace_Match_Winner import LogSquadTrace_Match_Winner
from Core.Plugins.LogSquadTrace_OnPossess import LogSquadTrace_OnPossess
from Core.Plugins.LogSquadTrace_OnUnPossess import LogSquadTrace_OnUnPossess
from Core.Plugins.LogSquadTrace_Vehicle_Damage import LogSquadTrace_Vehicle_Damage
from Core.Plugins.LogSquadTrace_Vehicle_Destroy import LogSquadTrace_Vehicle_Destroy
from Core.Plugins.LogSquadTrace_Wound import LogSquadTrace_Wound

def Log_Parser_SQL(database_info, server_id, log_address, date_today, LogNet_status, start_point):
    # Read the logs
    data, start_point = read_logs(log_address, start_point)
    # Using for function to loop the data
    for i in range(0, len(data)):
        # Split the original data by using "][" for getting the "action" and test whether the line is log
        # or something else
        text = data[i].split("][")
        # If length of text >2, means the server is successfully start
        if len(text) == 2:
            # Get the "action" info of the line
            action = (text[1].split(": "))[0].split("]")[1]
            # Get the "second action" info of the line
            try:
                sec_action = text[1].split(": ")[1]
                pass
            except:
                sec_action = "None"
                pass
            # For the line includes the action "LogNet"
            if action == "LogNet":
                # For the "second action" is the "Join request", which means the start of the player join, use
                # LogNet_request() to get info of the player name and mark the start of the player join
                if LogNet_status == 0 and sec_action == "Join request":
                    (date, time, Player_name, LogNet_status) = LogNet_request(data[i])
                    pass
                # For the "second action" is the "Join request", which means the start of the player join, use
                # LogNet_request() to get info of the player name and mark the start of the player join
                if LogNet_status == 1 and sec_action == "Join succeeded":
                    (date, time, Player_name, LogNet_status) = LogNet_succed(data[i])
                    Insert_SQL(database_info, "Log_Player_connect", date_today,
                               (date, time, Player_name, Player_64id, Player_controller, server_id))
                pass
            # For the line includes the action "LogOnline"
            if action == "LogOnline":
                # If the line contained the word "removed", use the LogOnline_disconnect() for logging the 64id of
                # disconnected player
                if ((text[1].split(": "))[2])[-10:-3] == "removed":
                    Insert_SQL(database_info, 'Log_Player_disconnect', date_today,
                               LogOnline_disconnect(data[i], server_id))
                pass
            # For the line includes the action "LogSquad"
            if action == "LogSquad":
                # If the line contained the word sets "ADMIN COMMAND", use LogSquad_Admin_cmd() for logging the usage of
                # Admin command
                if sec_action == "ADMIN COMMAND":
                    if len(((text[1].split(": "))[2]).split("Banned ")) == 2:
                        Insert_SQL(database_info, 'Log_Admin_Command', date_today,
                                   LogSquad_Admin_Ban(data[i], server_id))
                        pass
                    if len(((text[1].split(": "))[2]).split("Message broadcasted")) == 2:
                        Insert_SQL(database_info, 'Log_Admin_Command', date_today,
                                   LogSquad_Admin_broadcaste(data[i], server_id))
                        pass
                    if len(((text[1].split(": "))[2]).split("Change layer to")) == 2:
                        Insert_SQL(database_info, 'Log_Admin_Command', date_today,
                                   LogSquad_Admin_change_layer(data[i], server_id))
                        pass
                    if len(((text[1].split(": "))[2]).split("Remote admin disbanded")) == 2:
                        Insert_SQL(database_info, 'Log_Admin_Command', date_today,
                                   LogSquad_Admin_disband_squad(data[i], server_id))
                        pass
                    pass
                    if len(((text[1].split(": "))[2]).split("Forced team change for player")) == 2:
                        Insert_SQL(database_info, 'Log_Admin_Command', date_today,
                                   LogSquad_Admin_Forced_team_change(data[i], server_id))
                        pass
                    if len(((text[1].split(": "))[2]).split("Kicked ")) == 2:
                        Insert_SQL(database_info, 'Log_Admin_Command', date_today,
                                   LogSquad_Admin_Kick(data[i], server_id))
                        pass
                    if len(((text[1].split(": "))[2]).split("Set next layer to")) == 2:
                        Insert_SQL(database_info, 'Log_Admin_Command', date_today,
                                   LogSquad_Admin_set_layer(data[i], server_id))
                        pass
                    pass
                # If the line contained the word sets "(Steam I", use LogSquad_create_squad() for logging the info of
                # squad creator and the name of the squad
                if sec_action[-9:-1] == "(Steam I":
                    Insert_SQL(database_info, 'Log_Squads', date_today, LogSquad_create_squad(data[i], server_id))
                pass
                # If the line contained the word sets "Player", use LogSquad_Damage to log the damage log
                if sec_action[0:7] == "Player:":
                    Insert_SQL(database_info, 'Log_Battle_damage', date_today, LogSquad_Damage(data[i], server_id))
                pass
                # If the line contained the word sets "Success to ", use LogSquad_map() for logging the map rotation
                if sec_action[0:11] == "Success to ":
                    Insert_SQL(database_info, 'Log_Map_rotation', date_today, LogSquad_map(data[i], server_id))
                    pass
                # If the line contained the word sets "has revived", use LogSquad_revive() for logging the revive of
                # players in the battle
                if len(sec_action.split("has revived")) == 2:
                    Insert_SQL(database_info, 'Log_Battle_revive', date_today, LogSquad_revive(data[i], server_id))
                    pass
                # If the line contained the word "USQGameState", use LogSquad_Server_Tick_Rate for log the tick rate
                # of server
                if sec_action == "USQGameState":
                    Insert_SQL(database_info, 'Log_Server_Tick_Rate', date_today,
                               LogSquad_Server_Tick_Rate(data[i], server_id))
                    pass
                # If the line contained the word sets "PostLogin", use PostLogin() for logging Player_controller
                if LogNet_status == 1 and sec_action == "PostLogin":
                    (date, time, Player_controller) = LogSquad_PostLogin(data[i])
                    pass
            # For the line includes the action "LogEasyAntiCheatServer"
            if action == "LogEasyAntiCheatServer":
                try:
                    (date, time, Player_64id) = (LogEasyAntiCheatServer(data[i]))
                    pass
                except:
                    continue
                    pass
                pass
            if action == "LogSquadTrace":
                if sec_action == "[DedicatedServer]ASQPlayerController::OnPossess()":
                    if len((text[1].split(": "))[2].split("CameraMan")) == 4:
                        Insert_SQL(database_info, 'Log_CameraMan', date_today,
                                   LogSquadTrace_CameraMan(data[i], server_id))
                        pass
                    else:
                        Insert_SQL(database_info, 'Log_Possess', date_today,
                                   LogSquadTrace_OnPossess(data[i], server_id))
                        pass
                    pass
                if sec_action == "[DedicatedServer]ASQPlayerController::OnUnPossess()":
                    Insert_SQL(database_info, 'Log_UnPossess', date_today,
                               LogSquadTrace_OnUnPossess(data[i], server_id))
                    pass
                if sec_action == "[DedicatedServer]ASQSoldier::Die()":
                    Insert_SQL(database_info, 'Log_Battle_die', date_today, LogSquadTrace_Die(data[i], server_id))
                    pass
                if sec_action == "[DedicatedServer]ASQGameMode::DetermineMatchWinner()":
                    Insert_SQL(database_info, 'Log_Match_Winner', date_today,
                               LogSquadTrace_Match_Winner(data[i], server_id))
                    pass
                if sec_action == "[DedicatedServer]ASQVehicleSeat::TraceAndMessageClient()":
                    if (text[1].split(": ")[2])[0:15] == "SQVehicleSeat::":
                        continue
                        pass
                    elif (text[1].split(": ")[2])[0:15] == "SQVehicle::Take":
                        continue
                        pass
                    else:
                        Insert_SQL(database_info, 'Log_Battle_Vehicle_Damage', date_today,
                                   LogSquadTrace_Vehicle_Damage(data[i], server_id))
                        pass
                    pass
                if sec_action == "[DedicatedServer]ASQDestroyedVehicle::TakeDamage()":
                    if (text[1].split(": ")[2])[0:21] == "ASQDestroyedVehicle::":
                        continue
                        pass
                    else:
                        Insert_SQL(database_info, 'Log_Battle_Vehicle_Destroy', date_today,
                                   LogSquadTrace_Vehicle_Destroy(data[i], server_id))
                        pass
                    pass
                if sec_action == "[DedicatedServer]ASQDeployable::TakeDamage()":
                    if (text[1].split(": ")[2])[0:15] == "ASQDeployable::":
                        continue
                        pass
                    else:
                        Insert_SQL(database_info, 'Log_Battle_Deployable_Damage', date_today,
                                   LogSquadTrace_Deployable_Damage(data[i], server_id))
                        pass
                    pass
                if sec_action == "[DedicatedServer]ASQSoldier::Wound()":
                    Insert_SQL(database_info, 'Log_Battle_wound', date_today, LogSquadTrace_Wound(data[i], server_id))
                    pass
                pass
            pass
            print(i)
            pass
        pass
    t_ime.sleep(1)
    return start_point, LogNet_status
