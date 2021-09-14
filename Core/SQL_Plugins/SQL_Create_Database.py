import MySQLdb


def SQL_Create_Database(database_info, date_today):

    database_host = str(database_info["database_host"])
    database_port = int(database_info["database_port"])
    database_user = str(database_info["database_user"])
    database_passwd = str(database_info["database_passwd"])

    database_name = ('Log_Admin_Command', 'Log_Battle_damage', 'Log_Battle_Deployable_Damage', 'Log_Battle_die',
                     'Log_Battle_revive', 'Log_Battle_Vehicle_Damage',
                     'Log_Battle_Vehicle_Destroy', 'Log_Battle_wound', 'Log_Map_rotation', 'Log_Player_connect',
                     'Log_Player_disconnect', 'Log_Squads', 'Log_Possess', 'Log_UnPossess', 'Log_Match_Winner',
                     'Log_Rcon_AdminBan', 'Log_Rcon_AdminCamera', 'Log_Rcon_AdminDisbandSquad',
                     'Log_Rcon_AdminKick', 'Log_Rcon_Chat', 'Log_Rcon_PlayerInfo', 'Log_Rcon_TeamKill',
                     "Log_Server_Tick_Rate")

    # Create connection to database
    db = MySQLdb.connect(host=database_host, port=database_port, user=database_user, passwd=database_passwd,
                         charset='utf8mb4', autocommit=True)
    # Access the cursor by using cursor()
    mycursor = db.cursor()
    sql_create_table = str(0)
    # Checking the relative database/schema exists or not, if not, create the relative database
    for i in database_name:

        sql_create_database = "CREATE DATABASE IF NOT EXISTS " + i
        mycursor.execute(sql_create_database)
        if i == 'Log_Admin_Command':
            sql_create_table = "CREATE TABLE IF NOT EXISTS " + i + "." + "`" + date_today + "`" + \
                               " (Date VARCHAR(10) NOT NULL, " \
                               "Time VARCHAR(255) NOT NULL, " \
                               "CMD VARCHAR(255) NOT NULL, " \
                               "Info VARCHAR(255) NOT NULL, " \
                               "server_id VARCHAR(255) NOT NULL)"
            pass
        if i == 'Log_Battle_damage':
            sql_create_table = "CREATE TABLE IF NOT EXISTS " + i + "." + "`" + date_today + "`" + \
                               " (Date VARCHAR(10) NOT NULL, " \
                               "Time VARCHAR(255) NOT NULL, " \
                               "Player_take_damage VARCHAR(255) NOT NULL, " \
                               "Damage VARCHAR(255) NOT NULL, " \
                               "Player_make_damage VARCHAR(255) NOT NULL, " \
                               "Weapon VARCHAR(255) NOT NULL, " \
                               "server_id VARCHAR(255) NOT NULL)"
            pass
        if i == 'Log_Battle_Deployable_Damage':
            sql_create_table = "CREATE TABLE IF NOT EXISTS " + i + "." + "`" + date_today + "`" + \
                               " (Date VARCHAR(10) NOT NULL, " \
                               "Time VARCHAR(255) NOT NULL, " \
                               "Damage_taker VARCHAR(255) NOT NULL, " \
                               "Damage VARCHAR(255) NOT NULL, " \
                               "By_Weapon VARCHAR(255) NOT NULL, " \
                               "By_Player VARCHAR(255) NOT NULL, " \
                               "Damage_type VARCHAR(255) NOT NULL, " \
                               "Health_remain VARCHAR(255) NOT NULL, " \
                               "server_id VARCHAR(255) NOT NULL)"
            pass
        if i == 'Log_Battle_die':
            sql_create_table = "CREATE TABLE IF NOT EXISTS " + i + "." + "`" + date_today + "`" + \
                               " (Date VARCHAR(10) NOT NULL, " \
                               "Time VARCHAR(255) NOT NULL, " \
                               "Player_Victim_name VARCHAR(255), " \
                               "Damage FLOAT NOT NULL, " \
                               "Player_attacker_Controller VARCHAR(255), " \
                               "Weapon VARCHAR(255) NOT NULL, " \
                               "server_id VARCHAR(255) NOT NULL)"
            pass
        if i == 'Log_Battle_revive':
            sql_create_table = "CREATE TABLE IF NOT EXISTS " + i + "." + "`" + date_today + "`" + \
                               " (Date VARCHAR(10) NOT NULL, " \
                               "Time VARCHAR(255) NOT NULL, " \
                               "Player_Rescuer VARCHAR(255) NOT NULL, " \
                               "Player_Rescued VARCHAR(255) NOT NULL, " \
                               "server_id VARCHAR(255) NOT NULL)"
            pass
        if i == 'Log_Battle_Vehicle_Damage':
            sql_create_table = "CREATE TABLE IF NOT EXISTS " + i + "." + "`" + date_today + "`" + \
                               " (Date VARCHAR(10) NOT NULL, " \
                               "Time VARCHAR(255) NOT NULL, " \
                               "Destoryed_Vehichle VARCHAR(255) NOT NULL, " \
                               "Damage VARCHAR(255) NOT NULL, " \
                               "By_Weapon VARCHAR(255) NOT NULL, " \
                               "By_Player VARCHAR(255) NOT NULL, " \
                               "Health_remain VARCHAR(255) NOT NULL, " \
                               "server_id VARCHAR(255) NOT NULL)"
            pass
        if i == 'Log_Battle_Vehicle_Destroy':
            sql_create_table = "CREATE TABLE IF NOT EXISTS " + i + "." + "`" + date_today + "`" + \
                               " (Date VARCHAR(10) NOT NULL, " \
                               "Time VARCHAR(255) NOT NULL, " \
                               "Destoryed_Vehichle VARCHAR(255) NOT NULL, " \
                               "Damage VARCHAR(255) NOT NULL, " \
                               "By_Weapon VARCHAR(255) NOT NULL, " \
                               "By_Player VARCHAR(255) NOT NULL, " \
                               "Damage_type VARCHAR(255) NOT NULL, " \
                               "Health_remain VARCHAR(255) NOT NULL, " \
                               "server_id VARCHAR(255) NOT NULL)"
            pass
        if i == 'Log_Battle_wound':
            sql_create_table = "CREATE TABLE IF NOT EXISTS " + i + "." + "`" + date_today + "`" + \
                               " (Date VARCHAR(10) NOT NULL, " \
                               "Time VARCHAR(255) NOT NULL, " \
                               "Player_Victim_name VARCHAR(255), " \
                               "Damage FLOAT NOT NULL, " \
                               "Player_attacker_Controller VARCHAR(255), " \
                               "Weapon VARCHAR(255) NOT NULL, " \
                               "server_id VARCHAR(255) NOT NULL)"
            pass
        if i == 'Log_Map_rotation':
            sql_create_table = "CREATE TABLE IF NOT EXISTS " + i + "." + "`" + date_today + "`" + \
                               " (Date VARCHAR(10) NOT NULL, " \
                               "Time VARCHAR(255) NOT NULL, " \
                               "Level VARCHAR(255) NOT NULL, " \
                               "Layer VARCHAR(255) NOT NULL, " \
                               "server_id VARCHAR(255) NOT NULL)"
            pass
        if i == 'Log_Player_connect':
            sql_create_table = "CREATE TABLE IF NOT EXISTS " + i + "." + "`" + date_today + "`" + \
                               " (Date VARCHAR(10) NOT NULL, " \
                               "Time VARCHAR(255) NOT NULL, " \
                               "Player_name VARCHAR(255) NOT NULL, " \
                               "Steam_64ID VARCHAR(17) NOT NULL, " \
                               "PlayerController VARCHAR(255) NOT NULL, " \
                               "server_id VARCHAR(255) NOT NULL)"
            pass
        if i == 'Log_Player_disconnect':
            sql_create_table = "CREATE TABLE IF NOT EXISTS " + i + "." + "`" + date_today + "`" + \
                               " (Date VARCHAR(10) NOT NULL, " \
                               "Time VARCHAR(255) NOT NULL, " \
                               "Steam_64ID VARCHAR(17) NOT NULL, " \
                               "server_id VARCHAR(255) NOT NULL)"
            pass
        if i == 'Log_Squads':
            sql_create_table = "CREATE TABLE IF NOT EXISTS " + i + "." + "`" + date_today + "`" + \
                               " (Date VARCHAR(10) NOT NULL, " \
                               "Time VARCHAR(255) NOT NULL, " \
                               "Player_name VARCHAR(255) NOT NULL, " \
                               "Steam_64ID VARCHAR(17) NOT NULL, " \
                               "Squad_sequnce_num VARCHAR(255) NOT NULL, " \
                               "Player_Squad_name VARCHAR(255), " \
                               "Team_name VARCHAR(255) NOT NULL, " \
                               "server_id VARCHAR(255) NOT NULL)"
            pass
        if i == "Log_Possess":
            sql_create_table = "CREATE TABLE IF NOT EXISTS " + i + "." + "`" + date_today + "`" + \
                               " (Date VARCHAR(10) NOT NULL, " \
                               "Time VARCHAR(255) NOT NULL, " \
                               "Player_name VARCHAR(255) NOT NULL, " \
                               "Player_equip VARCHAR(255), " \
                               "server_id VARCHAR(255) NOT NULL)"
            pass
        if i == "Log_UnPossess":
            sql_create_table = "CREATE TABLE IF NOT EXISTS " + i + "." + "`" + date_today + "`" + \
                               " (Date VARCHAR(10) NOT NULL, " \
                               "Time VARCHAR(255) NOT NULL, " \
                               "Player_name VARCHAR(255) NOT NULL, " \
                               "server_id VARCHAR(255) NOT NULL)"
            pass
        if i == "Log_Match_Winner":
            sql_create_table = "CREATE TABLE IF NOT EXISTS " + i + "." + "`" + date_today + "`" + \
                               " (Date VARCHAR(10) NOT NULL, " \
                               "Time VARCHAR(255) NOT NULL, " \
                               "winner VARCHAR(255) NOT NULL, " \
                               "Layer VARCHAR(255), " \
                               "server_id VARCHAR(255) NOT NULL)"
            pass
        if i == 'Log_Rcon_AdminBan':
            sql_create_table = "CREATE TABLE IF NOT EXISTS " + i + "." + "`" + date_today + "`" + \
                               " (Date VARCHAR(10) NOT NULL, " \
                               "Time VARCHAR(255) NOT NULL, " \
                               "Admin_Name VARCHAR(255) NOT NULL, " \
                               "Admin_Steam_64id VARCHAR(255) NOT NULL, " \
                               "Banned_64id VARCHAR(255) NOT NULL, " \
                               "Banned_name VARCHAR(255) NOT NULL, " \
                               "Banned_interval VARCHAR(255) NOT NULL, " \
                               "server_id VARCHAR(255) NOT NULL)"
            pass
        if i == 'Log_Rcon_AdminCamera':
            sql_create_table = "CREATE TABLE IF NOT EXISTS " + i + "." + "`" + date_today + "`" + \
                               " (Date VARCHAR(10) NOT NULL, " \
                               "Time VARCHAR(255) NOT NULL, " \
                               "Player_64id VARCHAR(255) NOT NULL, " \
                               "Player_Name VARCHAR(255) NOT NULL, " \
                               "Chat_Content VARCHAR(255) NOT NULL, " \
                               "server_id VARCHAR(255) NOT NULL)"
            pass
        if i == 'Log_Rcon_AdminDisbandSquad':
            sql_create_table = "CREATE TABLE IF NOT EXISTS " + i + "." + "`" + date_today + "`" + \
                               " (Date VARCHAR(10) NOT NULL, " \
                               "Time VARCHAR(255) NOT NULL, " \
                               "squad_num VARCHAR(255) NOT NULL, " \
                               "team VARCHAR(255) NOT NULL, " \
                               "squad_name VARCHAR(255) NOT NULL, " \
                               "server_id VARCHAR(255) NOT NULL)"
            pass
        if i == 'Log_Rcon_AdminKick':
            sql_create_table = "CREATE TABLE IF NOT EXISTS " + i + "." + "`" + date_today + "`" + \
                               " (Date VARCHAR(10) NOT NULL, " \
                               "Time VARCHAR(255) NOT NULL, " \
                               "player_name VARCHAR(255) NOT NULL, " \
                               "kick_reason VARCHAR(255) NOT NULL, " \
                               "server_id VARCHAR(255) NOT NULL)"
            pass
        if i == 'Log_Rcon_Chat':
            sql_create_table = "CREATE TABLE IF NOT EXISTS " + i + "." + "`" + date_today + "`" + \
                               " (Date VARCHAR(10) NOT NULL, " \
                               "Time VARCHAR(255) NOT NULL, " \
                               "Chat_type VARCHAR(255) NOT NULL, " \
                               "Player_64id VARCHAR(255) NOT NULL, " \
                               "Player_name VARCHAR(255) NOT NULL, " \
                               "Chat_Content TEXT(65535) NOT NULL, " \
                               "server_id VARCHAR(255) NOT NULL)"
            pass
        if i == 'Log_Rcon_PlayerInfo':
            sql_create_table = "CREATE TABLE IF NOT EXISTS " + i + "." + "`" + date_today + "`" + \
                               " (Player_id VARCHAR(255) unique NOT NULL, " \
                               "Player_64id VARCHAR(255) NOT NULL, " \
                               "player_name VARCHAR(255) NOT NULL, " \
                               "player_team_id VARCHAR(255) NOT NULL, " \
                               "player_squad_id VARCHAR(255) NOT NULL, " \
                               "server_id VARCHAR(255) NOT NULL" \
                               ")"
            pass
        if i == 'Log_Rcon_TeamKill':
            sql_create_table = "CREATE TABLE IF NOT EXISTS " + i + "." + "`" + date_today + "`" + \
                               " (Date VARCHAR(10) NOT NULL, " \
                               "Time VARCHAR(255) NOT NULL, " \
                               "Player_attacker VARCHAR(255) NOT NULL, " \
                               "Player_victim VARCHAR(255) NOT NULL, " \
                               "Chat_Content TEXT(65535) NOT NULL, " \
                               "server_id VARCHAR(255) NOT NULL)"
            pass
        if i == "Log_Server_Tick_Rate":
            sql_create_table = "CREATE TABLE IF NOT EXISTS " + i + "." + "`" + date_today + "`" + \
                               " (Date VARCHAR(10) NOT NULL, " \
                               "Time VARCHAR(255) NOT NULL, " \
                               "Server_Tick_Rate VARCHAR(255) NOT NULL, " \
                               "server_id VARCHAR(255) NOT NULL)"
            pass
        mycursor.execute(sql_create_table)
        pass
    # Disconnect from the database
    db.close()
    pass