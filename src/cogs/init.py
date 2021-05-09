import discord
from discord.ext import commands

class Init(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game('Testing...'))
        print('We have logged in as {0.user}'.format(self.client))

    

def setup(client):
    client.add_cog(Init(client))