import discord
import config
import random

# LATER to use when I'm pulling different phrases from lists of possible responses?

TOKEN = config.TOKEN
switch = True

# Sets client & functions
client = discord.Client()


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    global switch
    print("Bananas...")
    if message.author == client.user:
        return
    msg = message.content
# Turns the bot off and on again (WE HOPE)
    if msg == "!off":
        switch = False
        await message.channel.send("ChitChatot has gone off to an expedition. Bye now!")
        print(switch)
    if msg == "!on":
        switch = True
        await message.channel.send("We have returned from our expedition! Squawk!")
        print(switch)
    print(switch)
# Bot talking routine
    if switch:
        if msg.startswith("!talk"):
            await message.channel.send("What would you like to talk about?")
        #await message.channel.send("Fred!")
        """
        if any(word in msg.lower() for word in money_words):
            await message.channel.send(random.choice(money_response))
        if any(word in msg.lower() for word in school_words):
            await message.channel.send(random.choice(school_response))
        if any(word in msg.lower() for word in sad_words):
            await message.channel.send(random.choice(sad_response))
        if any(word in msg.lower() for word in happy_words):
            await message.channel.send(random.choice(happy_response))
        """

# Wanted to try to get this code to work. Prev code works, but buggily

"""
     if msg == "!talk":
        await message.channel.send("What would you like to talk about?")
        if msg.startswith("!talk"):
            if any(word in msg.lower() for word in money_words):
                await message.channel.send(random.choice(money_response))
            if any(word in msg.lower() for word in school_words):
                await message.channel.send(random.choice(school_response))
            if any(word in msg.lower() for word in sad_words):
                await message.channel.send(random.choice(sad_response))
            if any(word in msg.lower() for word in happy_words):
                await message.channel.send(random.choice(happy_response))
"""

# Keywords and responses

happy_words = ["happy", "ecstatic", "good mood", "excited", "brain worms", "brain rot", "joy"]
happy_response = ["Squawk! ChitChatot is glad you're having fun.",
                  "I'm happy you're happy :smiling_face_with_3_hearts:",
                  "Treasure this! Joy is a gift."
                  "Enjoy life! :smiling_face_with_3_hearts:"]

school_words = ["school", "college", "university", "homework", "hw", "uni"]
school_response = ["School is hard. Then again, what would I know? I'm a bird.",
                   "Squawk! I graduated from Harvard."]

sad_words = ["depressed", "upset", "angry", "sad", "pissed", "unhappy", "miserable", "depressive", "depressing"]
sad_response = ["That's rough, buddy.",
                "What if I sent you out to gather Perfect Apples? Would that make you feel better?",
                "I'll give you something to cry about :triumph:",
                "I'm sorry that you're feeling bad."
                ]

money_words = ["money", "$", "dollars", "expensive"]
money_response = [
    "I'm sorry you feel that way my dear, but I don't think you're cut out for the rich life if you ask me",
    "lmao our guild is absolutely stacked :zany_face:",
    "All the extra bounty money goes to me and the Guildmaster, tee-hee!",
    "We run a very profitable busi- I mean organization.",
    "It's natural to have money troubles, even if it's not the source of your problems."]

# Runs the bot
client.run(TOKEN)

