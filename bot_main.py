import nextcord
import dotenv
import os.path
from nextcord.ext import commands

import cogs
import cogs.hoi
import cogs.misc
import cogs.oocqc

description = '''bot for the gay nerds server

literally may from pokemon

she has that name because her creator briefly considered may as a chosen name'''

if os.path.exists("./bot-config/description.txt"):
    with open("./bot-config/description.txt", "rt") as desc:
        description = desc.read() if desc.read() != "" else "custom help description file is empty. L bozo"

intents = nextcord.Intents.default()
intents.message_content = True

dotenv_file = dotenv.dotenv_values()

bot = commands.Bot(command_prefix=dotenv_file["BOT_PREFIX"], description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    bot.add_cog(cogs.hoi.HallOfInfamy(bot))
    bot.add_cog(cogs.misc.Misc(bot))
    bot.add_cog(cogs.oocqc.OOCQC(bot))
    await cogs.hoi.remove_unwanted_hoi_posts(bot)

TOKEN = dotenv_file["BOT_TOKEN"]
bot.run(TOKEN)
