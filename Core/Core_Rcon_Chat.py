import asyncio

from Core.SQL_Plugins.SQL_Insert import SQL_Insert
from Core.Rcon_Plugins.Rcon_Chat_Message import rcon_chat_message
from Core.Rcon_Plugins.Rcon_Chat_Chat import Rcon_Chat_Chat
from Core.Rcon_Plugins.Rcon_Chat_TeamKill import Rcon_Chat_TeamKill
from Core.Rcon_Plugins.Rcon_Chat_AdminBan import Rcon_Chat_AdminBan
from Core.Rcon_Plugins.Rcon_Chat_AdminCamera import Rcon_Chat_AdminCamera
from Core.Rcon_Plugins.Rcon_Chat_AdminKick import Rcon_Chat_AdminKick
from Core.Rcon_Plugins.Rcon_Chat_AdminDisbandSquad import Rcon_Chat_AdminDisbandSquad

class rconChatMesssage(asyncio):
    def __init__(self,database_info, date_today, server_rcon_info, threadID):
        self.server_rcon_info = server_rcon_info
        self.threadID = threadID
        self.database_info = database_info
        self.date_today = date_today
        self.server_name = list(server_rcon_info.keys())[threadID]
        self.server_id = server_rcon_info[self.server_name]['server_id']
        pass

    def run(self):
        chat_msg, chat_property = rcon_chat_message(
            server_rcon_info=self.server_rcon_info, server_name=self.server_name)
        if chat_property == 'Chat':
            SQL_Insert(database_info=self.database_info,
                       db_name='Log_Rcon_Chat',
                       table=self.date_today,
                       value=(Rcon_Chat_Chat(chat_msg=chat_msg, server_id=self.server_id)))
            pass
        elif chat_property == 'TeamKill':
            SQL_Insert(database_info=self.database_info,
                       db_name='Log_Rcon_TeamKill',
                       table=self.date_today,
                       value=(Rcon_Chat_TeamKill(chat_msg=chat_msg, server_id=self.server_id)))
            pass
        elif chat_property == 'AdminCamera':
            SQL_Insert(database_info=self.database_info,
                       db_name='Log_Rcon_AdminCamera',
                       table=self.date_today,
                       value=(Rcon_Chat_AdminCamera(chat_msg=chat_msg, server_id=self.server_id)))
            pass
        elif chat_property == 'AdminBan':
            SQL_Insert(database_info=self.database_info,
                       db_name='Log_Rcon_AdminBan',
                       table=self.date_today,
                       value=(Rcon_Chat_AdminBan(chat_msg=chat_msg, server_id=self.server_id)))
            pass
        elif chat_property == 'AdminDisbandSquad':
            SQL_Insert(database_info=self.database_info,
                       db_name='Log_Rcon_AdminDisbandSquad',
                       table=self.date_today,
                       value=(Rcon_Chat_AdminDisbandSquad(chat_msg=chat_msg, server_id=self.server_id)))
            pass
        elif chat_property == 'AdminKick':
            SQL_Insert(database_info=self.database_info,
                       db_name='Log_Rcon_AdminKick',
                       table=self.date_today,
                       value=(Rcon_Chat_AdminKick(chat_msg=chat_msg, server_id=self.server_id)))
            pass
        pass
    pass


