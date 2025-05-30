from email import message

import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

#Discord Bot Token Loading and Initialization
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

#Write mode
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='./', intents=intents)

#When code starts
@bot.event
async def on_ready():
    print("Hello World")

#When message
@bot.event
async def on_message(message):
    if message.author == bot.user: #invalid case
        return

    if "dbob" in message.content.lower():
        await message.delete()
        await message.channel.send(":(")

    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send(f"https://cdn.discordapp.com/emojis/816387537542053948.gif?size=64&quality=lossless")
    await ctx.delete()

@bot.command()
async def chess(ctx):
    await ctx.send("Chess")
#rule test
bot.run(token, log_handler=handler, log_level=logging.DEBUG)