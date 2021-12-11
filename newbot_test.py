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


@client.command()
async def talk(ctx, *, question):
    money_words = ["money", "$", "dollars", "expensive"]
    money_responses = [
        "I'm sorry you feel that way my dear, but I don't think you're cut out for the rich life if you ask me",
        "lmao our guild is absolutely stacked :zany_face:",
        "All the extra bounty money goes to me and the Guildmaster, tee-hee!",
        "We run a very profitable busi- I mean organization.",
        "It's natural to have money troubles, even if it's not the source of your problems."]

    happy_words = ["happy", "ecstatic", "good mood", "excited", "brain worms", "brain rot", "joy"]
    happy_responses = ["Squawk! ChitChatot is glad you're having fun.",
                       "I'm happy you're happy :smiling_face_with_3_hearts:",
                       "Treasure this! Joy is a gift.",
                       "Enjoy life! :smiling_face_with_3_hearts:"]

    school_words = ["school", "college", "university", "homework", "hw", "uni"]
    school_responses = ["School is hard. Then again, what would I know? I'm a bird.",
                        "Squawk! I graduated from Harvard."]

    sad_words = ["depressed", "upset", "angry", "sad", "pissed", "unhappy", "miserable", "depressive", "depressing"]
    sad_responses = ["That's rough, buddy.",
                     "What if I sent you out to gather Perfect Apples? Would that make you feel better?",
                     "I'll give you something to cry about :triumph:",
                     "I'm sorry that you're feeling bad."
                     ]
    general_responses = ["Squawk! (Chatot is not feeling very talkative today.)",
                         "What do you want to talk about?",
                         "Ask me about my 8-ball."]
    if question in sad_words:
        await ctx.send(random.choice(sad_responses))
    elif question in happy_words:
        await ctx.send(random.choice(happy_responses))
    elif question in money_words:
        await ctx.send(random.choice(money_responses))
    elif question in school_words:
        await ctx.send(random.choice(school_responses))
    else:
        await ctx.send(random.choice(general_responses))


# Test: Ping Pong
"""
@client.command()
async def ping(ctx):
    await ctx.send("pong!")
"""

client.run(TOKEN)
