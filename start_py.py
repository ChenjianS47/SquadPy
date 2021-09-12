import datetime
import time

from config import *
from Core.Core_main import threadLogParser
from Core.Core_Rcon_Chat import rconChatMesssage

# Get date of today
date_today = datetime.datetime.now().strftime('%Y.%m.%d')

threads = {}
rcon_threads = {}

for threadID in range(len(server_info)):
    threads[threadID] = threadLogParser(database_info=database_info, server_info=server_info,
                                        date_today=date_today, threadID=threadID)
    pass

for threadID in range(len(server_rcon)):
    rcon_threads[threadID] = rconChatMesssage(database_info=database_info, server_rcon_info=server_rcon,
                                              date_today=date_today, threadID=threadID)
    pass

while 1:
    print('{}, Checking the Thread is shutdown or not'.format(datetime.datetime.now().strftime("%H.%M.%S:%f")))
    for threadID in range(len(server_info)):
        if not threads[threadID].is_alive():
            threads[threadID].start()
            print("Reboot the "+str(list(server_info.keys())[threadID]))
            pass
        pass
    for threadID in range(len(server_rcon)):
        if not rcon_threads[threadID].is_alive():
            rcon_threads[threadID].start()
            print("Reboot the Rcon_Chat_receive"+str(list(server_rcon.keys())[threadID]))
            pass
    time.sleep(10)
    pass
pass
