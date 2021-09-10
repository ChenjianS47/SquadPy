import threading
from Core.Rcon_Plugins.Rcon_Chat_Message import rcon_chat_message
from Core.Plugins.Insert_SQL import Insert_SQL
import datetime

class rconChatMesssage(threading.Thread):
    def __init__(self,database_info, date_today, server_rcon_info, threadID):
        threading.Thread.__init__(self)
        self.server_rcon_info = server_rcon_info
        self.threadID = threadID
        self.database_info = database_info
        self.date_today = date_today
        self.server_name = list(server_rcon_info.keys())[threadID]
        self.server_id = server_rcon_info[self.server_name]['server_id']
        pass

    def run(self):
        while 1:
            chat_type, Player_64id, Player_name, chat_content = rcon_chat_message(
                server_rcon_info=self.server_rcon_info, server_name=self.server_name)
            Insert_SQL(database_info=self.database_info,
                       db_name='Log_Server_Chat_Message',
                       table=self.date_today,
                       value=(datetime.datetime.now().strftime("%Y.%m.%d"),
                              datetime.datetime.now().strftime("%H.%M.%S:%f"),
                              chat_type,
                              Player_64id,
                              Player_name,
                              chat_content,
                              self.server_id))
            pass
        pass
    pass


