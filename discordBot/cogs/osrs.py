import discord
from osrs_api.const import AccountType
from osrs_api import Hiscores
from discord.ext import commands

class OSRS(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def osrs(self, ctx, *, username):
        username = str(username)
        user = Hiscores(username)
        user = user.skills
        embedVar = discord.Embed(title="OSRS Stats for "+ username)
        for i in user:
            embedVar.add_field(name=user[i].name, value=user[i].level)
        await ctx.send(embed = embedVar)
        #add error when user doesnt exit

def setup(client):
    client.add_cog(OSRS(client))