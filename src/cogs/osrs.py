import discord
import os
import sys
from PIL import Image
from osrs_api.const import AccountType
from osrs_api import Hiscores
from osrs_api import GrandExchange
from osrsbox import items_api
from discord.ext import commands
from osrsbox.items_api.item_properties import ItemProperties
from converters.itemObject import ItemConverter


class OSRS(commands.Cog):
    def __init__(self, client):
        self.client = client

    #searches OSRS items database for ID of item provided by user in userItem
    @commands.command()
    async def itemid(self, ctx, *, userItem: ItemConverter):
        await ctx.send(f'the item id for {userItem.name} is {userItem.id}')


    @commands.command(aliases=['Stats'])
    async def stats(self, ctx, *, username):
        username = str(username)
        try:
            user = Hiscores(username)
        except:
            await ctx.send('There is no OSRS player named ' + username)
        else:
            user = user.skills

            skills = ('attack', 'hitpoints', 'mining', 'strength', 'agility',
                    'smithing', 'defence', 'herblore', 'fishing', 'ranged',
                    'thieving', 'cooking', 'prayer', 'crafting', 'firemaking',
                    'magic', 'fletching', 'woodcutting', 'runecrafting', 'slayer',
                    'farming','construction','hunter')
            embedVar = discord.Embed(title="OSRS Stats for "+ username)
            total = 0
            for i,j in enumerate(skills):
                embedVar.add_field(name=user[j].name.capitalize(), value=user[j].level)
                total +=user[j].level
            embedVar.add_field(name='Total', value=total)

            await ctx.send( embed=embedVar)

    @stats.error
    async def stats_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please provide a username')

    
    @commands.command(aliases=['Ge', 'GE'])
    async def ge(self, ctx, *, userItem: ItemConverter):
        await ctx.send('test')

def setup(client):
    client.add_cog(OSRS(client))