# ~ SushiCatBot ~

A Discord Bot using [Discord.py](https://discordpy.readthedocs.io/en/stable/)

**Requirments:**

* [Python3](https://www.python.org/downloads/)

**Setup:**

Run **init.py** to set up the bot and initialise the database. You need to add your own bot token to the **api_tokens.py** file. Also add the channel id of the channel you want the birthday messages to be printed in. There is a bot trap function as well where you can add a channel id, and the bot will ban anyone sending a message in that channel.

Get the bot token by setting up your own discord app at https://discord.com/developers

For the weather command, you need an API key from https://openweathermap.org/

---

**Commands:**

* **!help** : Sends the command list in a DM to the user. Also posts a link to the repo in the channel.

* **!loot** : Does a simple MMO loot roll, giving a number from 1 to and including 100.

* **!register name birthday (E.g. John 1997-08-29)** : Registers a name and birthday for the user, and saves it to the database.

* **!unregister** : Removes the user from the database.

* **!profile** : Shows the name and birthday registered by the user.

* **!slowmode seconds** : Turns on slow mode for the channel, with the given seconds as the delay.

* **!weather location** : Prints out the temperature and condition for the provided location.

* **!d4** : Throws a 4-sided dice.

* **!d6** : Throws a 6-sided dice.

* **!d8** : Throws an 8-sided dice.

* **!d10** : Throws a 10-sided dice.

* **!d12** : Throws a 12-sided dice.

* **!d20** : Throws a 20-sided dice.

* **!d00** : Throws a percentage dice.
