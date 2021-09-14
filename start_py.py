import datetime
import time
import asyncio

from config import *
from Core.Core_main import threadLogParser
from Core.Core_Rcon_Chat import rconChatMesssage
from Core.Core_Rcon_UpdatingPlayerInfo import rconUpdatingPlayerInfo

# Get date of today
date_today = datetime.datetime.now().strftime('%Y.%m.%d')
t = 0
threads = {}
rcon_threads = {}
rcon_threads_player = {}

for threadID in range(len(server_info)):
    threads[threadID] = threadLogParser(database_info=database_info,
                                        server_info=server_info,
                                        date_today=date_today,
                                        threadID=threadID)
    pass
for threadID in range(len(server_rcon)):
    print('Recivev the Chat {}'.format(list(server_rcon.keys())[threadID]))
    rcon_threads[threadID] = rconChatMesssage(database_info=database_info,
                                              server_rcon_info=server_rcon,
                                              date_today=date_today,
                                              threadID=threadID,
                                              waring_info_TeamKill=waring_info_TeamKill)
    pass


while 1:
    # print('{}, Checking the Thread is shutdown or not'.format(datetime.datetime.now().strftime("%H.%M.%S:%f")))
    for threadID in range(len(server_info)):
        if not threads[threadID].is_alive():
            threads[threadID].start()
            print("Reboot the log reader " + str(list(server_info.keys())[threadID]))
            pass
        if not rcon_threads[threadID].is_alive():
            rcon_threads[threadID].start()
            print("Reboot the chat reciver " + str(list(server_info.keys())[threadID]))
            pass
        pass
    pass

