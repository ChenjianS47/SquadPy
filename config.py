# Input the database into this block
database_info = {"database_host": "127.0.0.3",
                 "database_port": 3306,
                 "database_user": "test",
                 "database_passwd": "test"
                 }



# Input the server info in this block
server_info = {
    "server_1": {"server_id": 1, "server_log": "D:/servers/squad_server_1/SquadGame/Saved/Logs/SquadGame.log"},
    "server_5": {"server_id": 5, "server_log": "D:/servers/squad_server_5/SquadGame/Saved/Logs/SquadGame.log"}
}

# Inpu the server rcon info in this block
server_rcon = {
    "server_1": {"server_id": 1, 'Server_IP': '0.0.0.0', 'RCON_Port': int(21115), 'Server_pw': 'yourpassword'},
    "server_5": {"server_id": 5, 'Server_IP': '0.0.0.0', 'RCON_Port': int(21117), 'Server_pw': 'yourpassword'}
}