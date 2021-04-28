import discord
import logging

logging.basicConfig(level=logging.INFO)
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == '':
        await message.channel.send('#nial4life: ' + str(nialCounter))

client.run('ODM2MzYyMjU4OTA0MzgzNTQ5.YIc5DQ.PW9C_q9Av1oGZMKnEU8W6eB5O7I')