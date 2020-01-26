#!/usr/bin/env python

import os
import discord

from minecraft import \
    get_minecraft_status_message, \
    get_minecraft_ping_message, \
    get_minecraft_open_message, \
    get_minecraft_close_message, \
    get_minecraft_host_message

def get_hello_message(): return 'Hello!'

client = discord.Client()

responders = {
    "hello": get_hello_message,
    "minecraft-status": get_minecraft_status_message,
    "minecraft-ping": get_minecraft_ping_message,
    "minecraft-open": get_minecraft_open_message,
    "minecraft-close": get_minecraft_close_message,
    "minecraft-host": get_minecraft_host_message,
    "mcs": get_minecraft_status_message,
    "mcp": get_minecraft_ping_message,
    "mco": get_minecraft_open_message,
    "mcc": get_minecraft_close_message,
    "mch": get_minecraft_host_message,
}

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = None
    for responder_name in responders:
        if message.content.startswith('$' + responder_name):
            responder = responders[responder_name]
            if responder:
                msg = responder()
            break

    if message.content.startswith('$help'):
        msg = 'Commands:\n'
        for responder_name in responders:
            msg += '$' + responder_name + '\n'

    if msg is not None:
        await message.channel.send(msg)

token = os.environ['AKALEE_TOKEN']

client.run(token)
