import threading
import datetime
from Core.Base.Log_Parser_SQL import Log_Parser_SQL
from Core.Plugins.create_sql_database import create_sql_database

class threadLogParser(threading.Thread):
    def __init__(self, database_info, server_info, date_today, threadID):
        threading.Thread.__init__(self)
        self.LogNet_status = 0
        self.start_point = 0
        self.last_point = 0
        self.threadID = threadID
        self.database_info = database_info
        self.date_today = date_today
        self.server_name = list(server_info.keys())[threadID]
        self.server_id = server_info[self.server_name]['server_id']
        self.server_log = server_info[self.server_name]['server_log']
        pass

    def run(self):
        while 1 > 0:
            # Create the datebase when the program starts
            create_sql_database(self.database_info, self.date_today)
            print("updating the log of server {} to SQL {}".format(
                self.server_name, datetime.datetime.now().strftime('%H:%M:%S')))
            try:
                self.start_point, self.LogNet_status = Log_Parser_SQL(database_info=self.database_info,
                                                            server_id=self.server_id,
                                                            log_address=self.server_log,
                                                            date_today=self.date_today,
                                                            LogNet_status=self.LogNet_status,
                                                            start_point=self.start_point)
                pass
            except:
                self.start_point, self.LogNet_status = Log_Parser_SQL(database_info=self.database_info,
                                                            server_id=self.server_id,
                                                            log_address=self.server_log,
                                                            date_today=self.date_today,
                                                            LogNet_status=self.LogNet_status,
                                                            start_point=self.last_point)
                pass
            self.last_point = self.start_point
            pass
        pass
    pass
