# ~ SushiCatBot ~

A Python Discord Bot using Discord.py

https://discordpy.readthedocs.io/en/stable/

**Requirments:**

Python3: https://www.python.org/downloads/

SQLite3: https://sqlite.org/

**Startup:**

Run **init.py** to set up the bot and initialise the database. You need to add your own bot token to the BOT_TOKEN.py file. Also add the channel id of the channel you want the birthday messages to be printed in.

Get the bot token by setting up your own discord app at https://discord.com/developers

**Commands:**

**!help** : Prints a link to this repo.

**!loot** : Does a simple MMO loot roll, giving a number from 1 to and including 100.

**!register name birthday (E.g. John 1997-08-29)** : Registers a name and birthday for the user calling the command, and saves it to the database.

**!unregister** : Removes the user calling the command, from the database.

**!profile** : Shows the name and birthday registered by the user calling the command.

**!d4** : Throws a 4-sided dice.

**!d6** : Throws a 6-sided dice.

**!d8** : Throws an 8-sided dice.

**!d10** : Throws a 10-sided dice.

**!d12** : Throws a 12-sided dice.

**!d20** : Throws a 20-sided dice.

**!d00** : Throws a percentage dice.
