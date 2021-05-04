import discord
import logging
import json

logging.basicConfig(level=logging.INFO)
client = discord.Client()
counter = 0

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == '#nial4life':
        global counter 
        counter = counter + 1
        data = {}
        data['nial4life'] = []
        data['nial4life'].append({'counter' : counter})

        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)
        await message.channel.send('#nial4life: ' + str(counter) )

client.run('ODM2MzYyMjU4OTA0MzgzNTQ5.YIc5DQ.PW9C_q9Av1oGZMKnEU8W6eB5O7I')