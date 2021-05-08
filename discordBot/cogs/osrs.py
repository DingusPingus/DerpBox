import discord
from osrs_api.const import AccountType
from osrs_api import Hiscores
from discord.ext import commands

class OSRS(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def osrs(self, ctx, *, username):
        await ctx.send('fetching stats for ' + str(username) + "...")
        user = Hiscores(username)
        await ctx.send(user.skills['attack'].level)
        #add error when user doesnt exit

def setup(client):
    client.add_cog(OSRS(client))