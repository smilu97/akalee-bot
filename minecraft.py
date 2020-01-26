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
    message = "The server has {0} players and replied in {1} ms".format(status.players.online, status.latency)
    return message

def get_minecraft_ping_message():
    if check_server_dead(): return MSG_SERVER_IS_DEAD
    ping = get_minecraft_ping()
    message = "The server replied in {0} ms".format(ping)    
    return message

def get_minecraft_query_message():
    if check_server_dead(): return MSG_SERVER_IS_DEAD
    query = get_minecraft_query()
    message = "The server has the following players online: {0}".format(", ".join(query.players.names))
    return message

def get_minecraft_open_message():
    open_minecraft()
    return 'Attempted to open minecraft server'

def get_minecraft_close_message():
    close_minecraft()
    return 'Attempted to close minecraft server'
    
