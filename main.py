from email import message
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import asyncio

from chess_game import position_verification
#custom imports
from chess_pieces import Piece
from board import Board

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
    board1 = Board()
    board1.printTable()
    game_msg = await ctx.send(board1)

    def verify_challenge(w):
        return w.author == ctx.author and w.channel == ctx.channel and w.mentions

    def verify_player1(w):
        return w.author == ctx.author and w.channel == ctx.channel

    def verify_player2(w):
        return w.author == ctx.author and w.channel == ctx.channel

    try:
        #Chess challenge procedure
        msg = await bot.wait_for("message", check=verify_challenge, timeout=30.0)
        player1 = ctx.author
        player2 = msg.mentions[0]
        await ctx.send(f"{player1.mention} vs {player2.mention}")

    except asyncio.TimeoutError:
        await ctx.send("Timed out")

    #Chess Game
    while True:
        msg = await bot.wait_for("message", check=verify_player1, timeout=30.0)
        if msg.content.lower() == "move":
            board1.move(4,6,4,4)
            await game_msg.edit(content=board1)
        elif msg.content.lower() == "quit":
            print("quit")
            break
        elif msg.content.lower() == "help":
            print("help")
        elif position_verification(msg.content, board1):
            print("pos verif")
            await game_msg.edit(content=board1)
        else:
            print("fail")
        #test
        print("ignored")

        #game logic
        #./chess
        #challenge w @
        #bot sends a challenge message
        #player 1 goes
        #move gets deleted
        #bot changes the challenge message to player 2 turn
        #player 2 goes
        #move gets deleted
        #bot changes the chal msg to player 1 turn

bot.run(token, log_handler=handler, log_level=logging.DEBUG)