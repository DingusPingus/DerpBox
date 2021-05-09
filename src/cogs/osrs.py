import discord
from PIL import Image
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
        
        skills = ('attack', 'hitpoints', 'mining', 'strength', 'agility',
                 'smithing', 'defence', 'herblore', 'fishing', 'ranged',
                 'thieving', 'cooking', 'prayer', 'crafting', 'firemaking',
                 'magic', 'fletching', 'woodcutting', 'runecrafting', 'slayer',
                 'farming','construction','hunter')
        embedVar = discord.Embed(title="OSRS Stats for "+ username)
        file = discord.File('../assets/osrsIcons/osrsicons.png', filename ='image.png')
        embedVar.set_image(url='attachment://image.png')
        total = 0
        for i,j in enumerate(skills):
            embedVar.add_field(name=user[j].name, value=user[j].level)
            total +=user[j].level
        embedVar.add_field(name='total', value=total)

        await ctx.send(file=file, embed=embedVar)

def setup(client):
    client.add_cog(OSRS(client))