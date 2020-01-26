import json
import os

from mcstatus import MinecraftServer

server = MinecraftServer.lookup('15.165.167.41:25565')

MSG_SERVER_IS_DEAD = 'The server is dead'

def open_minecraft():
    os.popen('tmux new -d -s minecraft /home/ubuntu/run.sh')

def close_minecraft():
    os.popen('tmux kill-session -t minecraft')

def check_server_dead():
    try:
        latency = server.ping()
        return False
    except:
        return True

def get_minecraft_status():
    return server.status()

def get_minecraft_ping():
    return server.ping()

def get_minecraft_query():
    return server.query()

def get_minecraft_status_message():
    if check_server_dead(): return MSG_SERVER_IS_DEAD
    status = get_minecraft_status()
    message = f"The server has {status.players.online} players and replied in {status.latency} ms"
    return message

def get_minecraft_ping_message():
    if check_server_dead(): return MSG_SERVER_IS_DEAD
    ping = get_minecraft_ping()
    message = f"The server replied in {ping} ms"
    return message

def get_minecraft_query_message():
    if check_server_dead(): return MSG_SERVER_IS_DEAD
    query = get_minecraft_query()
    message = f"The server has the following players online: {', '.join(query.players.names)}"
    return message

def get_minecraft_open_message():
    open_minecraft()
    return 'Attempted to open minecraft server'

def get_minecraft_close_message():
    close_minecraft()
    return 'Attempted to close minecraft server'
    
