import discord
from discord.ext import commands

Wonderbot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@Wonderbot.event
async def on_ready():
    print("Wonderbot ready")

with open("token.txt") as file:
    token = file.read()

Wonderbot.run(token)


