import discord
import config
from discord.ext import commands

TOKEN = config.TOKEN

client = commands.Bot(command_prefix="!")
@client.event
async def on_ready():
    print("We are GOING.")

client.run(TOKEN)