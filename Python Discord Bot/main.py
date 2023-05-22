import discord
from discord import app_commands
from discord.ext import commands
from perspective import PerspectiveAPI
import logging
import os
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.DEBUG)
the_one_that_bad = []
number_of_bad_word_they_say = []
BOT_TOKEN = os.getenv("BOT_TOKEN")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
p = PerspectiveAPI(str(GOOGLE_API_KEY))

def check_if_toxic(text):
    result = p.score(text)
    toxicity_score = round(result["TOXICITY"], 2)
    return toxicity_score > 0.75

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
prefix = "at!"
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print("\nRunning discord.py library version", discord.__version__)
    print(f"\nWe have logged in as {bot.user}!")
    guild = bot.guilds[0]
    guild_id = guild.id
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="every word you say"))
    print(f"{bot.user} is ready to go!")
    print(f"Bot connected to server ID: {guild_id}")
    print(f"\nPerspective API is ready to go!")

@bot.event
async def on_message(message):
    content = message.content
    author = message.author
    index = the_one_that_bad.index(author)
    if author not in the_one_that_bad:
        the_one_that_bad.append(author)
        number_of_bad_word_they_say.append(1)
    else:
        number_of_bad_word_they_say[index] += 1
    if content == prefix + "help":
        embed = embed = discord.Embed(title="This is what I can do:", color=discord.Color.yellow())
        embed.description = "at!help - You are seeing it right now!\nat!mute (username)\nat!unmute (userid mention or mention) - Unmute the user specified"
        await message.channel.send(embed=embed)
        return

    # Check if the message starts with the command prefix and the command is "mute"
    if content.startswith(prefix + "mute"):
        # Extract the username from the message content
        username = content.split(maxsplit=1)[1]

        # Send the response
        await message.channel.send(f"Muting user: {username}")

        # Delete the user's command message
        await message.delete()
        return

    if author == bot.user or message.author.bot:
        print("Message from [BOT]:", author, ":", content)
        return

    print("Message from:", author, ":", content)
    is_toxic = check_if_toxic(content)
    if is_toxic:
        await message.channel.send(f"{author.mention}, watch your words!")
    if number_of_bad_word_they_say[index] == 3:
        await message.channel.send(f"Hey {author.mention}! You have been warned! If you say 2 more, you will be temporarily suspended from sending messages and joining voice chat channels on this server.")
        await message.channel.send(
            "After you are suspended, only a moderator can help you!"
        )
        await message.channel.send(f"{author.mention}, YOU HAVE BEEN WARNED! DON'T ASK WHY I'M EVIL WHEN IT HAPPENS!")
    if number_of_bad_word_they_say[index] == 5:
        del number_of_bad_word_they_say[index]
        del the_one_that_bad[index] 
        await message.channel.send(f"{author.mention}, enjoy the temporary suspension!")
        role = discord.utils.get(message.guild.roles, name="Member")
        await message.author.remove_roles(role)
        await message.channel.send(f"Role '{role.name}' removed from {message.author.mention}.")

    await bot.process_commands(message)

bot.run(str (BOT_TOKEN))
