import discord
import sqlite3
import re
import os
import traceback
from discord.ext import commands

class Nial(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['nial4life','nial','Nial', 'NialCount', 'nialcount'])
    async def nialCount(self, ctx):
        db = sqlite3.connect(os.path.realpath('../data/database/counters.db'))
        c = db.cursor()
        nialCounter = c.execute("SELECT * FROM Counters WHERE name = '#nial4life' ").fetchone()[1]
        nialCounter += 1
        c.execute("UPDATE Counters SET val =" + str(nialCounter)+ " WHERE name ='#nial4life' ")
        db.commit()
        await ctx.send('#nial4life: ' + str(nialCounter))
        db.close()

    @commands.command(aliases=['NialRank','Nialrank', 'nialrank'])
    async def nialRank(self, ctx, *, member: discord.Member=None):
        if member is None:
            member = ctx.author

        db = sqlite3.connect(os.path.realpath('../data/database/counters.db'))
        c = db.cursor()
        rank = c.execute('SELECT * FROM NialCount WHERE guildID = ? AND userID =?',(ctx.guild.id, member.id)).fetchone()
        db.close()
        await ctx.send(f'{member.name} has typed {rank[2]} nials')
        
    @nialRank.error
    async def nialRank_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You must mention the user or provide their id as an argument.')

    @commands.command(aliases=['NialTop','Nialtop','nialtop'])
    async def nialTop(self, ctx):
        db = sqlite3.connect(os.path.realpath('../data/database/counters.db'))
        c = db.cursor()
        ranks = c.execute('SELECT * FROM NialCount WHERE guildID = ? ORDER BY nialCount DESC LIMIT 10',(ctx.guild.id,)).fetchall()
        db.close()
        embedVar = discord.Embed(title="nial leaderboards")
        for row in ranks:
            member = ctx.message.guild.get_member(row[1])
            embedVar.add_field(name=member.name, value=row[2], inline=False)
        await ctx.send(embed=embedVar)
   
    @commands.Cog.listener()
    async def on_message(self, message):
        if(message.author.id != self.client.user.id):
            channel = message.channel
            nialCount = len(re.findall("nial", message.content, re.IGNORECASE))
            if (nialCount > 0):
                db = sqlite3.connect(os.path.realpath('../data/database/counters.db'))
                c = db.cursor()
                c.execute("INSERT OR IGNORE INTO NialCount(guildID, userID) VALUES(?,?)",(message.guild.id, message.author.id))
                c.execute("UPDATE NialCount SET nialCount = nialCount + ? WHERE guildID = ? AND userID = ?",(nialCount, message.guild.id, message.author.id))
                db.commit()
                db.close()

            
def setup(client):
    client.add_cog(Nial(client))
