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


@client.command(aliases=['8ball'],
                help="Picks a random response to a given message.",
                brief="A magic 8 ball with a twist."
                )
async def eightball(ctx, *, question):
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
                 "try again tomorrow, maybe i'll tell you tomorrow...",
                 'ask again later.',
                 'better not tell you now.',
                 'cannot predict now.',
                 'go ponder your orb about it.',
                 'concentrate and ask again.',
                 'do not count on it.',
                 'i suggest to not go near that shit',
                 'my reply is no.',
                 'my sources say no.',
                 'outlook not so good.',
                 'very doubtful.',
                 'it is my earnest recommendation not to.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command(help="Picks randomly from a list of prompts.",
                brief="A handy way to get some inspiration.")
async def prompt(ctx):
    prompt_list = ["What does it mean to be a vessel?",
                   "Think about the associations you have with a song. What are those associations?",
                   "Pick a color that is immediately in your sight. What is compelling about it?",
                   "Pick a dream.",
                   "What does it feel like not to be able to see? Does it bother you? Does it free you?",
                   "Imagine a door. What does the door look like, and where is it located? Where does it go?",
                   "The compulsions of an article of clothing.",
                   "Your favorite old building.",
                   "Digging.",
                   "A household object that unsettles you. Mine is the mirror.",
                   "Your favorite part of your favorite movie, and why",
                   "The meaning of a diary entry",
                   "A spice you favor, for any reason",
                   "fruity",
                   "And now, the weather.",
                   "*airhorn noises* E-E-E-EXTREME SPORTS!",
                   "An old painting",
                   "Ode",
                   "Anagram",
                   "Muse",
                   "Garden",
                   "The mutability of a fairy tale",
                   "The seasons",
                   "secret message",
                   "Sainthood in any meaning of the word",
                   "Something on your YouTube favorites list",
                   "Deserter",
                   "Stranded",
                   "Cactus",
                   "Flower Language",
                   "Spies",
                   "Boat (raft, sailboat, Titanic, etc)",
                   "Your favorite number (mine is 64)",
                   "'-ology' fields",
                   "Treehouse",
                   "A particulary competitive and deadly game [of monopoly]",
                   "Look up your favorite word in the thesaurus and see what happens",
                   "childhood pet",
                   "What would you see if you stood on the roof right now?",
                   "Parody an iconic shakespeare scene",
                   "Sea Monster"
                   ]
    await ctx.send(random.choice(prompt_list))


@client.command(help="Depending on the keywords you use, Chatot will spit out a phrase corresponding to the mood.",
                brief="Chatot will tell you what's on his mind.")
async def talk(ctx, *, question):
    money_words = ["money", "$", "dollars", "expensive"]
    money_responses = [
        "I'm sorry you feel that way my dear, but I don't think you're cut out for the rich life if you ask me",
        "lmao our guild is absolutely stacked :zany_face:",
        "All the extra bounty money goes to me and the Guildmaster, tee-hee!",
        "We run a very profitable busi- I mean organization.",
        "It's natural to have money troubles, even if it's not the source of all your problems."]

    happy_words = ["happy", "ecstatic", "good mood", "excited", "brain worms", "brain rot", "joy"]
    happy_responses = ["Squawk! ChitChatot is glad you're having fun.",
                       "I'm happy you're happy :smiling_face_with_3_hearts:",
                       "Treasure this! Joy is a gift.",
                       "Enjoy life! :smiling_face_with_3_hearts:",
                       "Smiles go for miles!"
                       ]

    school_words = ["school", "college", "university", "homework", "hw", "uni"]
    school_responses = ["School is hard. Then again, what would I know? I'm a bird.",
                        "Squawk! I graduated from Harvard.",
                        "Don't shirk work!"]

    sad_words = ["depressed", "upset", "angry", "sad", "pissed", "unhappy", "miserable", "depressive", "depressing"]
    sad_responses = ["That's rough, buddy.",
                     "What if I sent you out to gather Perfect Apples? Would that make you feel better?",
                     "I'll give you something to cry about :triumph:",
                     "I'm sorry that you're feeling bad."
                     ]
    general_responses = ["Squawk! (Chatot is not feeling very talkative today.)",
                         "What do you want to talk about?",
                         "Ask me about my 8-ball.",
                         "Run away and pay!",
                         "you reposted in the wrong neighborhood",
                         "I'm sure, given enough time, I could come up with a good pun."
                         "Did you know I can dispense writing prompts?"]

    if any(word in question for word in sad_words):
        await ctx.send(random.choice(sad_responses))
    elif any(word in question for word in happy_words):
        await ctx.send(random.choice(happy_responses))
    elif any(word in question for word in money_words):
        await ctx.send(random.choice(money_responses))
    elif any(word in question for word in school_words):
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
