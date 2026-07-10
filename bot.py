import discord
from discord.ext import commands
import random
import database
from bot_token import BOT_TOKEN # Keep this in .gitignore
from constants import VALID_DICE

intents = discord.Intents.default()
intents.members = True   # REQUIRED to receive member join events

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


# Prints a message to the cli upon going online on Discord.
@bot.event
async def on_ready():
    print("Hello! SushiCatBot is ready! o7")


# Prints a welcome message to new members joining the sever; in a channel called welcome.
@bot.event
async def on_member_join(member):
    channel_name = "welcome"  # replace with your channel name

    for ch in member.guild.text_channels:
        if ch.name == channel_name:
            await ch.send(f"Welcome {member.mention} !")
            break


# Simple MMO loot roll.
@bot.command()
async def loot(ctx):
    result = random.randint(1, 100)
    await ctx.send(f"{ctx.author.mention} rolled **{result}** !")


# Rolls a tabletop dice with command: !d<roll>. Checks for valid dice.
@bot.event
async def on_message(message):
    content = message.content
    if content.startswith("!d"):
        arg = content[2:]
        roll = int(arg)

        if roll not in VALID_DICE:
            await message.channel.send("Not a valid dice!")
            return

        elif roll == 00:
            result = random.randint(1, 100)
            await message.channel.send(f"ᕕ( ᐛ )ᕗ {message.author.mention} rolled **{result}%** !")
            return

        else:
            result = random.randint(1, roll)

            if result == roll:
                await message.channel.send(f"ᕕ( ᐛ )ᕗ {message.author.mention} rolled a natural **{result}** !!!")
            elif result == 1:
                await message.channel.send(f"ᕕ( ᐛ )ᕗ {message.author.mention} rolled a natural **{result}**.. :(")
            else:
                await message.channel.send(f"ᕕ( ᐛ )ᕗ {message.author.mention} rolled **{result}** !")
            return

bot.run(BOT_TOKEN)