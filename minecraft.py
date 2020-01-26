import json

from mcstatus import MinecraftServer

server = MinecraftServer.lookup('15.165.167.41:25565')

def get_minecraft_status():
    return server.status()

def get_minecraft_ping():
    return server.ping()

def get_minecraft_query():
    return server.query()

def get_minecraft_status_message():
    status = get_minecraft_status()
    message = "The server has {0} players and replied in {1} ms".format(status.players.online, status.latency)
    return message

def get_minecraft_ping_message():
    ping = get_minecraft_ping()
    message = "The server replied in {0} ms".format(ping)    
    return message

def get_minecraft_query_message():
    query = get_minecraft_query()
    message = "The server has the following players online: {0}".format(", ".join(query.players.names))

    return message
