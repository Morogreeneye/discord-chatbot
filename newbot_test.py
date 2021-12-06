import discord
import config
import random
from discord.ext import commands

TOKEN = config.TOKEN

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print("We are GOING.")


@client.event
async def on_member_join(member):
    # await message.channel.send
    print(f"Squawk! Hello, {member}!")


@client.event
async def on_member_remove(member):
    print(f"{member} has left.")


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['it is certain.',
                 'it is decidedly so.',
                 'without a doubt.',
                 'yes, most definitely.',
                 'you may rely on it.',
                 'as i see it, yes.',
                 'most likely.',
                 'outlook good.',
                 'yes.',
                 'signs point to yes.',
                 'reply hazy, try again.',
                 'ask again later.',
                 'better not tell you now.',
                 'cannot predict now.',
                 'concentrate and ask again.',
                 'do not count on it.',
                 'i suggest to not go near that shit',
                 'my reply is no.',
                 'my sources say no.',
                 'outlook not so good.',
                 'very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


# Test: Ping Pong
"""
@client.command()
async def ping(ctx):
    await ctx.send("pong!")
"""

client.run(TOKEN)
