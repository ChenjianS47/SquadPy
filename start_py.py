import datetime
import time
import threading

from config import *
from Core.Core_main import threadLogParser


# Get date of today
date_today = datetime.datetime.now().strftime('%Y.%m.%d')



threads = {}

for threadID in range(len(server_info)):
    threads[threadID] = threadLogParser(database_info=database_info, server_info=server_info,
                          date_today=date_today, threadID=threadID)
    pass

while 1 > 0:
    print('Checking the Thread is shutdwon or not')
    for threadID in range(len(server_info)):
        if not threads[threadID].is_alive():
            threads[threadID].start()
            print("Reboot the "+str(list(server_info.keys())[threadID]))
            pass
        pass
    time.sleep(1)
    pass
pass

