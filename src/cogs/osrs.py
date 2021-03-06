import discord
import os
import sys
import requests
import base64
from requests.exceptions import HTTPError
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
        try:
            await ctx.send(f'the item id for {userItem.name} is {userItem.id}')
        except AttributeError:
            await ctx.send('invalid ID or name provided')

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
    async def stats_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please provide a valid username')

    
    @commands.command(aliases=['Ge', 'GE'])
    async def ge(self, ctx, *, userItem: ItemConverter):

        #https://pynative.com/parse-json-response-using-python-requests-library/
        if(userItem.tradeable_on_ge):
            try:
                url = 'http://prices.runescape.wiki/api/v1/osrs/latest?id='
                headers ={
                    'User-Agent': 'simple discord bot GE lookup - @%uD83D%uDCA9Dingus%uD83D%uDCA9#5352'
                }
                response = requests.get(url +str(userItem.id), headers=headers)
                response.raise_for_status()
                itemData_json = response.json()['data'][str(userItem.id)]
            except HTTPError as http_err: 
                print(f'HTTP error occurred: {http_err}')
            except Exception as err:
                print(f'Other error occurred: {err}')
           
            embedVar = discord.Embed(title=userItem.name, description=userItem.examine, colour=discord.Colour.lighter_grey())
            embedVar.set_thumbnail(url='https://raw.githubusercontent.com/runelite/static.runelite.net/gh-pages/cache/item/icon/'+str(userItem.id)+'.png') \
                    .add_field(name='high', value=itemData_json['high']) \
                    .add_field(name='low', value=itemData_json['low'])
            await ctx.send(embed=embedVar)
        else:
            await ctx.send('That item is not tradeable on the GE')
        

    @ge.error
    async def ge_error(self, ctx, error):
        if isinstance(error, AttributeError):
            await ctx.send('invalid ID or name provided')
        

def setup(client):
    client.add_cog(OSRS(client))