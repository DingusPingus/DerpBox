import discord
import sqlite3
import re
import traceback
from discord.ext import commands

class Nial(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['nial4life','nial','Nial', 'NialCount', 'nialcount'])
    async def nialCount(self, ctx):
        db = sqlite3.connect('counters.db')

        c = db.cursor()
        nialCounter = c.execute("SELECT * FROM Counters WHERE name = '#nial4life' ").fetchone()[1]
        nialCounter += 1
        c.execute("UPDATE Counters SET val =" +str(nialCounter)+ " WHERE name ='#nial4life' ")
        db.commit()
        await ctx.send('#nial4life: ' + str(nialCounter))
        db.close

    @commands.Cog.listener()
    async def on_message(self, message):
        if(message.author.id != self.client.user.id):
            channel = message.channel
            nialCount = len(re.findall("nial", message.content))
            if (nialCount > 0):
                await channel.send('progress')

            
def setup(client):
    client.add_cog(Nial(client))
