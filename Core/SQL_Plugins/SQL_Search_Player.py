import MySQLdb

def SQL_Search_Player(database_info, db_name, table, value):
    database_host = str(database_info["database_host"])
    database_port = int(database_info["database_port"])
    database_user = str(database_info["database_user"])
    database_passwd = str(database_info["database_passwd"])
    db_excute = MySQLdb.connect(host=database_host, port=database_port, user=database_user, passwd=database_passwd,
                                charset='utf8mb4', autocommit=True)
    cursor = db_excute.cursor()
    try:
        sql_insert_data = "SELECT Player_64id FROM " + db_name + "." + "`" + table + "`" + " where player_name like " +\
                          "'%" + str(value) + "%'" + ";"
        pass
    except:
        db_excute.ping()
        cursor = db_excute.cursor()
        sql_insert_data = "SELECT Player_64id FROM " + db_name + "." + "`" + table + "`" + " where player_name like " +\
                          "'%" + str(value) + "%'" + ";"
    cursor.execute(sql_insert_data)
    steam_64id = cursor.fetchone()
    db_excute.close()
    return steam_64id

