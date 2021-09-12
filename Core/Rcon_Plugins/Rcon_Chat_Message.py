import Core.Base.pyscrds_modified as rcon

# Define a function that recive the chat info of the server


def rcon_chat_message(server_rcon_info,server_name):
    conn = rcon.RconConnection(server=server_rcon_info[server_name]['Server_IP'],
                               port=server_rcon_info[server_name]['RCON_Port'],
                               password=server_rcon_info[server_name]['Server_pw'])
    chat_msg, chat_property = conn.receive_chat_message()
    return chat_msg, chat_property
    pass




