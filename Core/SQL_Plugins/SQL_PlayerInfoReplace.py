import MySQLdb
import time

def SQL_PlayerInfoReplace(database_info, db_name, table, value):
    database_host = str(database_info["database_host"])
    database_port = int(database_info["database_port"])
    database_user = str(database_info["database_user"])
    database_passwd = str(database_info["database_passwd"])
    db_excute = MySQLdb.connect(host=database_host, port=database_port, user=database_user, passwd=database_passwd,
                                charset='utf8mb4', autocommit=True)
    cursor = db_excute.cursor()
    try:
        sql_replace_data = "INSERT INTO " + db_name + "." + "`" + table + "`" + " " +\
                           '(player_id, player_64id, player_name, player_team_id, player_squad_id, server_id)' +\
                           'VALUES ' + str(value) + ' ' + \
                           'on duplicate key update ' + 'player_id = ' + '\'' + str(value[0]) + '\'' + ',' + \
                           'player_64id=' + '\'' + str(value[1]) + '\'' + ',' \
                           'player_name=' + '\'' + str(value[2]) + '\'' + ',' \
                           'player_team_id=' + '\'' + str(value[3]) + '\'' + ',' \
                           'player_squad_id=' + '\'' + str(value[4]) + '\'' + ',' \
                           'server_id =' + '\'' + str(value[5]) + '\'' + ";"
        pass
    except:
        db_excute.ping()
        cursor = db_excute.cursor()
        sql_replace_data = "INSERT INTO " + db_name + "." + "`" + table + "`" + " " + \
                           '(player_id, player_64id, player_name, player_team_id, player_squad_id, server_id)' + \
                           'VALUES ' + str(value) + ' ' + \
                           'on duplicate key update ' + 'player_id = ' + '\'' + str(value[0]) + '\'' + ',' + \
                           'player_64id=' + '\'' + str(value[1]) + '\'' + ',' \
                           'player_name=' + '\'' + str(value[2]) + '\'' + ',' \
                           'player_team_id=' + '\'' + str(value[3]) + '\'' + ',' \
                           'player_squad_id=' + '\'' + str(value[4]) + '\'' + ',' \
                           'server_id =' + '\'' + str(value[5]) + '\'' + ";"
        pass
    cursor.execute(sql_replace_data)
    db_excute.close()
    time.sleep(0.01)
    pass