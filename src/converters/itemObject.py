import discord
from discord.ext import commands
from osrsbox import items_api

class ItemConverter(commands.Converter):
    async def convert(self, ctx, argument):
        items = items_api.load()
        try:
            argument = int(argument)
            print('test')
            for item in items:
                if(item.id == argument):
                    return item 
        except ValueError:
            pass #value not int so must be string       
        try:
            for item in items:
                if(item.name.lower() == argument.lower()):
                    return item
        except:
            await ctx.send('invalid ID or name provided')
            raise commands.BadArgument(message='invalid ID or name provided')
        