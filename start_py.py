import datetime

from config import *
from Core.Core_main import threadLogParser
from Core.Plugins.create_sql_database import create_sql_database

date_today = datetime.datetime.now().strftime('%Y.%m.%d')

create_sql_database(database_info, date_today)

for threadID in range(len(server_info)):
    locals()['Process_' + str(threadID)] = threadLogParser(database_info=database_info,server_info=server_info,
                                                           date_today=date_today, threadID=threadID).start()
    pass