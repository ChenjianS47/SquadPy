import MySQLdb
import time

def Insert_SQL(database_info, db_name, table, value):
    database_host = str(database_info["database_host"])
    database_port = int(database_info["database_port"])
    database_user = str(database_info["database_user"])
    database_passwd = str(database_info["database_passwd"])
    db_excute = MySQLdb.connect(host=database_host, port=database_port, user=database_user, passwd=database_passwd,
                                charset='utf8mb4', autocommit=True)
    cursor = db_excute.cursor()
    try:
        sql_insert_data = "INSERT INTO " + db_name + "." + "`" + table + "`" + " VALUES" + str(value) + ";"
        pass
    except:
        db_excute.ping()
        cursor = db_excute.cursor()
        sql_insert_data = "INSERT INTO " + db_name + "." + "`" + table + "`" + " VALUES" + str(value) + ";"
        pass
    cursor.execute(sql_insert_data)
    db_excute.close()
    time.sleep(0.01)
    pass