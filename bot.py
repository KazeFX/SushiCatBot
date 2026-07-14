import datetime
import discord
from discord.ext import commands, tasks
import random
import database_helper
from bot_token import BOT_TOKEN, BIRTHDAY_MESSAGE_CHANNEL_ID # Keep this in .gitignore
from constants import VALID_DICE


intents = discord.Intents.default()
intents.members = True   # REQUIRED to receive member join events
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
bot.help_command = None

# Prints a message to the cli upon going online on Discord
@bot.event
async def on_ready():
    print("Hello! SushiCatBot is ready! o7")
    birthday_check.start()
    print("Birthday task started.")


# Prints a welcome message to new members joining the sever; in a channel called welcome
@bot.event
async def on_member_join(member):
    channel_name = "welcome"  # replace with your channel name
    for ch in member.guild.text_channels:
        if ch.name == channel_name:
            await ch.send(f"Welcome {member.mention} !")
            break


# Posts a link to the bot github with instructions and commands
@bot.command()
async def help(ctx):
    await ctx.send(f"Bot manual can be found at: https://github.com/KazeFX/SushiCatBot")


# Simple MMO loot roll
@bot.command()
async def loot(ctx):
    result = random.randint(1, 100)
    if result == 100:
        await ctx.send(f"OMG!! {ctx.author.mention} rolled **{result}** !!")
    else:
        await ctx.send(f"{ctx.author.mention} rolled **{result}** !")


# Register a name and birthday and connect it to a discord user id
@bot.command()
async def register(ctx, name: str, birthday: str):
    database_helper.add_user(ctx.author.id, name, birthday)
    await ctx.send(f"Saved {name} with birthday {birthday}")


# Deletes the user from the database; that runs the command
@bot.command()
async def unregister(ctx):
    database_helper.delete_user(ctx.author.id)
    await ctx.send(f"Removed {ctx.author.mention} from the database.")


# Prints in the channel, the saved information about the user calling the command
@bot.command()
async def profile(ctx, member: discord.Member = None):
    member = member or ctx.author
    row = database_helper.get_user(member.id)
    if row:
        await ctx.send(
            f"User: {row['name']}\nBirthday: {row['birthday']}"
        )
    else:
        await ctx.send("No data found for this user!")


# Bot task that runs every minute, checks birthdays at 09:00 every day and prints out a birthday message in
# the channel specified in BIRTHDAY_MESSAGE_CHANNEL_ID
@tasks.loop(minutes=1)
async def birthday_check():
    now = datetime.datetime.now()
    if now.hour == 9 and now.minute == 0: # Run at specific time, here 09:00
        birthdays = database_helper.get_birthdays_today()
        if not birthdays:
            return
        channel = bot.get_channel(BIRTHDAY_MESSAGE_CHANNEL_ID)
        for user_id, bday in birthdays:
            user = await bot.fetch_user(user_id)
            await channel.send(f"🎉 Happy Birthday, {user.mention}! 🎂")


# Rolls a tabletop dice with command: !d<roll>. Checks for valid dice
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
    await bot.process_commands(message)


bot.run(BOT_TOKEN)