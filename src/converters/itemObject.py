import discord
from discord.ext import commands
from osrsbox import items_api

class ItemConverter(commands.Converter):
    async def convert(self, ctx, argument):
        items = items_api.load()
        if(isinstance(argument, int)):
            for item in items:
                if(item.id == argument):
                    return item         
        elif(isinstance(argument, str)):
            for item in items:
                if(item.name.lower() == argument.lower()):
                    return item
        
        raise commands.BadArgument(message='invalid ID or name provided')