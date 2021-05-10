import discord
import os
import sys
from PIL import Image
from osrs_api.const import AccountType
from osrs_api import Hiscores
from osrs_api import GrandExchange
from osrsbox import items_api
from discord.ext import commands

class OSRS(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['Stats'])
    async def stats(self, ctx, *, username):
        username = str(username)
        try:
            user = Hiscores(username)
        except:
            await ctx.send('There is no player named ' + username)
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

    @commands.command(aliases=['Ge', 'GE'])
    async def ge(self, ctx, *, userInput):
        userInput = str(userInput)
        items = items_api.load()
        try:
            for item in items:
                if(item.name == userInput and item.duplicate == false):
                    userItem = item.name
        except:
            await ctx.send('The item' + userInput + 'does not exist, make sure you have provided the correct name!')
        #make it so its not so low querying the entire item database if id is already provided

def setup(client):
    client.add_cog(OSRS(client))