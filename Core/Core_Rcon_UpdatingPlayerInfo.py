import re
import asyncio


from Core.Rcon_Plugins.Rcon_ListPlayers import Rcon_ListPlayers
from Core.Rcon_Plugins.Rcon_AdminListDisconnectPlayers import Rcon_AdminListDisconnectPlayers
from Core.SQL_Plugins.SQL_PlayerInfoReplace import SQL_PlayerInfoReplace

class rconUpdatingPlayerInfo(asyncio):
    def __init__(self,database_info, date_today, server_rcon_info, threadID):
        self.server_rcon_info = server_rcon_info
        self.threadID = threadID
        self.database_info = database_info
        self.date_today = date_today
        self.server_name = list(server_rcon_info.keys())[threadID]
        self.server_id = server_rcon_info[self.server_name]['server_id']
        pass

    def run(self):
        info = Rcon_ListPlayers(server_rcon_info=self.server_rcon_info, server_name=self.server_name)[:-2]
        print(info)
        for i in info.split('\\n'):
            if re.search(r'ID: (.*) \| SteamID: (.*) \| Name: (.*) \| Team ID: (.*) \| Squad ID: (.*)', i,
                         re.S | re.M) is not None:
                matchobj = re.search(r'ID: (.*) \| SteamID: (.*) \| Name: (.*) \| Team ID: (.*) \| Squad ID: (.*)',
                                     i, re.S | re.M)
                player_id = matchobj.group(1)
                player_64id = matchobj.group(2)
                player_name = matchobj.group(3)
                player_team_id = matchobj.group(4)
                player_squad_id = matchobj.group(4)
                server_id = self.server_id
                SQL_PlayerInfoReplace(database_info=self.database_info,
                                      db_name='Log_Rcon_PlayerInfo',
                                      table=self.date_today,
                                      value=(
                                      player_id, player_64id, player_name, player_team_id, player_squad_id, server_id))
                pass
            pass
        info_dis = Rcon_AdminListDisconnectPlayers(server_rcon_info=self.server_rcon_info,
                                                   server_name=self.server_name)[:-2]
        for g in info_dis.split('\\n'):
            if re.search(r'ID: (.*) \| SteamID: (.*) \| Since Disconnect: (.*) \| Name: (.*)', g,
                         re.S | re.M) is not None:
                matchobj = re.search(r'ID: (.*) \| SteamID: (.*) \| Since Disconnect: (.*) \| Name: (.*)', g,
                                     re.S | re.M)
                player_id = matchobj.group(1)
                player_64id = 'NULL'
                player_name = 'NULL'
                player_team_id = 'NULL'
                player_squad_id = 'NULL'
                server_id = self.server_id
                SQL_PlayerInfoReplace(database_info=self.database_info,
                                      db_name='Log_Rcon_PlayerInfo',
                                      table=self.date_today,
                                      value=(
                                      player_id, player_64id, player_name, player_team_id, player_squad_id, server_id))
                pass
            pass
        pass
    pass
