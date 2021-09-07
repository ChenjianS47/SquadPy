import datetime

from Core.Plugins.create_sql_database import create_sql_database
from Core.Base.Log_Parser_SQL import Log_Parser_SQL

date_today = datetime.datetime.now().strftime('%Y.%m.%d')

database_info = {"database_host": "127.0.0.3",
                 "database_port": 3306,
                 "database_user": "foreconadmin",
                 "database_passwd": "foreconadmin123!@#"
                 }
server_id = 1

log_address = "D:/servers/squad_server_1/SquadGame/Saved/Logs/SquadGame.log"


# Init the param that stands for the start/end of the player join
LogNet_status = 0
# Init the start point of the log
start_point = 0

last_point = 0

system_on = 1


create_sql_database(database_info, date_today)

while system_on > 0:
    print("updating the log to SQL {}".format(datetime.datetime.now().strftime('%H:%M:%S')))
    try:
        start_point, LogNet_status = Log_Parser_SQL(database_info=database_info,
                                                    server_id=server_id,
                                                    log_address=log_address,
                                                    date_today=date_today,
                                                    LogNet_status=LogNet_status,
                                                    start_point=start_point)
        pass
    except:
        start_point, LogNet_status = Log_Parser_SQL(database_info=database_info,
                                                    server_id=server_id,
                                                    log_address=log_address,
                                                    date_today=date_today,
                                                    LogNet_status=LogNet_status,
                                                    start_point=last_point)
        pass
    last_point = start_point
    pass
