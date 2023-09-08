import discord
from discord import app_commands
from discord.ext import commands
import logging
import os
from dotenv import load_dotenv

load_dotenv()
logginglevel = "DEBUG"
logging.basicConfig(level=logging.DEBUG)
the_one_that_bad = []
number_of_bad_word_they_say = []
BOT_TOKEN = os.getenv("BOT_TOKEN")

print(BOT_TOKEN)
print(str(BOT_TOKEN))

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
prefix = "at!"
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print('Bot is online')
    guild = bot.guilds[0]
    guild_id = guild.id
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="sieunhanhxanhpgd get spammed"))
    return

async def on_message(message):
    await message.channel.send("<@961216418160992286>")
    print("message received")
    await bot.process_commands(message)

bot.run(str (BOT_TOKEN))
