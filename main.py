import discord

import discord
TOKEN = "OTE0OTY1ODI1NDA3MDQxNjQ2.YaUuVA.hbjtLuXgLH3z58m7KlTNGFqVxRU"

#Sets client & functions
client= discord.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

#Runs the bot
client.run(TOKEN)