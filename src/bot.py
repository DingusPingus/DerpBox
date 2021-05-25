import discord
import sqlite3
import os
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '$', intents = intents)

@client.command()
async def load(ctx, extension):
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'loaded {extension} cog')

@client.command()
async def unload(ctx, extension):
        client.unload_extension(f'cogs.{extension}')
        await ctx.send(f'unloaded {extension} cog')

@client.command()
async def reload(ctx, extension):
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'reloaded {extension} cog')

for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
                client.load_extension(f'cogs.{filename[:-3]}')


client.run('ODM2MzYyMjU4OTA0MzgzNTQ5.YIc5DQ.PW9C_q9Av1oGZMKnEU8W6eB5O7I')