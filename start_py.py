import datetime
import time
import asyncio

from config import *
from Core.Core_main import threadLogParser
from Core.Core_Rcon_Chat import rconChatMesssage
from Core.Core_Rcon_UpdatingPlayerInfo import rconUpdatingPlayerInfo

# Get date of today
date_today = datetime.datetime.now().strftime('%Y.%m.%d')

threads = {}
rcon_threads = {}
rcon_threads_player = {}

print(date_today)

async def async_threadLogParser(database_info, server_info, date_today, threadID):
    await threadLogParser(database_info=database_info, server_info=server_info, date_today=date_today, threadID=threadID)
    pass

async def async_rconChatMesssage(database_info, server_rcon, date_today, threadID):
    await rconChatMesssage(database_info=database_info, server_rcon_info=server_rcon,
                           date_today=date_today, threadID=threadID)
    pass

async def async_rconUpdatingPlayerInfo(database_info, server_rcon, date_today, threadID):
    await rconUpdatingPlayerInfo(database_info=database_info, server_rcon_info=server_rcon,
                                 date_today=date_today, threadID=threadID)
    pass


async def main():
    for threadID in range(len(server_info)):
        threads[threadID] = asyncio.create_task(async_threadLogParser(database_info=database_info,
                                                                      server_info=server_info,
                                                                      date_today=date_today,
                                                                      threadID=threadID))
        pass

    for threadID in range(len(server_rcon)):
        rcon_threads[threadID] = asyncio.create_task(async_rconChatMesssage(database_info=database_info,
                                                                            server_rcon=server_rcon,
                                                                            date_today=date_today,
                                                                            threadID=threadID))
        pass

    for threadID in range(len(server_rcon)):
        rcon_threads_player[threadID] = asyncio.create_task(async_rconUpdatingPlayerInfo(database_info=database_info,
                                                                                         server_rcon=server_rcon,
                                                                                         date_today=date_today,
                                                                                         threadID=threadID))
        pass
    while 1:
        for threadID in range(len(server_info)):
            print('Reading the log {}'.format(list(server_info.keys())[threadID]))
            await threads[threadID]
            await asyncio.sleep(1)
            pass
        for threadID in range(len(server_rcon)):
            print('Recivev the Chat {}'.format(list(server_rcon.keys())[threadID]))
            await rcon_threads[threadID]
            await asyncio.sleep(1)
            print('updating the playerinfo {}'.format(list(server_rcon.keys())[threadID]))
            await rcon_threads_player[threadID]
            await asyncio.sleep(1)
            pass
        pass
    pass

asyncio.run(main())