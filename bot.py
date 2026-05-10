import discord
import array
from discord.ext import commands
import random
from bot_token import BOT_TOKEN
from constants import VALID_DICE


bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Hello! SushiCatBot is ready! o7")


# Adds two number together.
@bot.command()
async def add(ctx, *arr):
    result = 0
    for i in arr:
        result += int(i)
    await ctx.send(str(result))


@bot.command()
async def sub(ctx, *arr):
    result = 0
    for i in arr:
        result -= int(i)
    await ctx.send(str(result))


@bot.command()
async def on_member_join(self, member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = f'Welcome {member.mention} to {guild.name}!'
        await guild.system_channel.send(to_send)


@bot.command()
async def d(ctx, *arr):
    roll = int(arr[0])

    if roll not in VALID_DICE:
        await ctx.send("Not a valid dice!")
        return

    elif roll == 00:
        result = random.randint(1, 100)
        await ctx.send(f"ᕕ( ᐛ )ᕗ You rolled **{result}%** !")
        return

    else:
        result = random.randint(1, roll)

        if result == roll:
            await ctx.send(f"ᕕ( ᐛ )ᕗ You rolled a natural **{result}** !!!")
        elif result == 1:
            await ctx.send(f"ᕕ( ᐛ )ᕗ You rolled a natural **{result}**.. :(")
        else:
            await ctx.send(f"ᕕ( ᐛ )ᕗ You rolled **{result}** !")
        return

bot.run(BOT_TOKEN)
