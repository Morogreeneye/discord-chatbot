import discord

import discord
#import random LATER to use when I'm pulling different phrases from lists of possible responses?
TOKEN = "OTE0OTY1ODI1NDA3MDQxNjQ2.YaUuVA.hbjtLuXgLH3z58m7KlTNGFqVxRU"

#Sets client & functions
client= discord.Client()

#Currently unused keywords
#school_words = ["school", "college", "university", "homework", "hw", "uni"]
#sad_words = ["depressed", "upset", "angry", "sad", "pissed", "unhappy", "miserable", "depressive", "depressing"]
money_words = ["money", "$", "dollars", "expensive"]
money_response = "I'm sorry you feel that way my dear, but I don't think you're cut out for the rich life if you ask me"

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg=message.content
    if msg.startswith("!talk"):
        await message.channel.send("What would you like to talk about?")
    if any(word in msg for word in money_words):
        await message.channel.send(money_response)

#Wanted to try to get this code to work. Prev code works, but buggily

"""
   if msg == "!talk":
        await message.channel.send("What would you like to talk about?")
        if msg.startswith("!talk"):
            if any(word in msg for word in money_words):
                await message.channel.send(money_response)
"""

#Runs the bot
client.run(TOKEN)