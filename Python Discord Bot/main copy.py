import discord
from discord.ext import commands
import json
import requests

BOT_TOKEN = "MTEwNzk5MzgxMDM0NjE4MDcyMw.GPxWvH.a3hTDIiDB6yyHROkaTO54Qyihq52QsCNUuMRfg"
GOOGLE_API_KEY = "AIzaSyAxX9F8UKqpMQiuVgs-DuIgW-iAlJWLbx0"

def content_moderation(text):
    url = 'https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze?key=' + GOOGLE_API_KEY
    data = {
        'comment': {'text': text},
        'requestedAttributes': {'TOXICITY': {}}
    }
    response = requests.post(url, data=json.dumps(data))
    result = response.json()

    toxicity_score = round(result['attributeScores']['TOXICITY']['summaryScore']['value'], 2)
    if toxicity_score > 0.9:
        return True
    else:
        return False

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="at!", intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name="at!help - Anti-Toxic Bot is ready"))
    print(f"We have logged in as {bot.user}!")

@bot.event
async def on_message(message):
    if message.author == bot.user or message.author.bot:
        return

    print(f"Message from {message.author}: {message.content}")
    is_toxic = content_moderation(message.content)
    if is_toxic:
        await message.channel.send(f"{message.author.mention}, watch your words!")

@bot.command()
async def setup(ctx):
    if not ctx.author.guild_permissions.manage_channels:
        await ctx.send("You don't have the necessary permissions to set up the logs channel.")
        return

    await ctx.send("Please mention the channel you want to set as the logs channel.")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        channel_message = await bot.wait_for("message", check=check, timeout=60)  # Wait for the user's response for 60 seconds
    except asyncio.TimeoutError:
        await ctx.send("Timed out. Please try again.")
        return

    logs_channel = channel_message.channel_mentions[0] if channel_message.channel_mentions else None

    if logs_channel is None:
        await ctx.send("Invalid channel mentioned. Please try again.")
        return

    with open("logs_channel.txt", "w") as file:
        file.write(str(logs_channel.id))

    await ctx.send(f"Logs channel set to {logs_channel.mention}.")

bot.run(BOT_TOKEN)