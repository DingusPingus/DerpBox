import discord
import sqlite3
import os
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '$', intents = intents)

db = sqlite3.connect('counters.db')

c = db.cursor()

# c.execute("""CREATE TABLE Counters(
#             name text,
#             val integer
#             )""")

# c.execute("""INSERT INTO Counters(name, val) VALUES('#nial4life', 0)""")
# db.commit()




@client.command()
async def load(ctx, extension):
        client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
        client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
                client.load_extension(f'cogs.{filename[:-3]}')





@client.command(aliases=['nial4life'])
async def nial(ctx):
        nialCounter = c.execute("SELECT * FROM Counters WHERE name = '#nial4life' ").fetchone()[1]
        nialCounter += 1
        c.execute("UPDATE Counters SET val =" +str(nialCounter)+ " WHERE name ='#nial4life' ")
        db.commit()
        await ctx.send('#nial4life: ' + str(nialCounter))

client.run('ODM2MzYyMjU4OTA0MzgzNTQ5.YIc5DQ.PW9C_q9Av1oGZMKnEU8W6eB5O7I')
db.close()