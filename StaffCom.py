import sqlite3
import asyncio
from datetime import datetime
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
bot = commands.bot(command_prefix="/", intents=intents, help_command=None) 

@bot.event
async def on_ready():
    db = sqlite3.connect("warning.sqlite")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS warnings(user INTERGER, reason TEXT, time INTERGER, guild INTERGER)")
    print("Wonderbot is online") 


async def addwarn(ctx, reason, user):
        db = sqlite3.connect("warn.sqlite")
        cursor = db.cursor()
        cursor.execute("INSERT INTO warnings (reason, user, time guild) VALUES (?, ?, ?, ?)", (user.id, reason, int(datetime.now().timestamp(), ctx.guild.id)))
        db.commit()


@bot.commands()
@commands.has_permissions(moderator=True)
async def warn(ctx, member:discord.Member, *, reason:str = "no reason"):
      await addwarn(ctx, reason, member)
      await ctx.send(f"Warned {member.mention} for {reason}")
      
      db = sqlite3.connect("warning.sqlite")
      cursor =db.cursor()
      cursor.execute("SELECT * FROM warnings WHERE user = ? AND guild = ?", (member.id, ctx.guild.id))
      data = cursor.fetchall() 
      if len(data) >= 1:
            await ctx.send (f"You have been warned {len(data)} time")
            await asyncio.sleep(0)

            db = sqlite3.connect("warning.sqlite")
      cursor =db.cursor()
      cursor.execute("SELECT * FROM warnings WHERE user = ? AND guild = ?", (member.id, ctx.guild.id))
      data = cursor.fetchall() 
      if len(data) >= 2:
            muteRole =  discord.utils.get(ctx.guild.roles, name="Muted")
            await member.add_roles(muteRole)
            await ctx.send (f"You have been warned {len(data)} time and you are now temp muted")
            await asyncio.sleep(900)
            await member.remove_roles(muteRole)
            await ctx.send (f"{member.mention} You have been unmuted")
            
            db = sqlite3.connect("warning.sqlite")
      cursor =db.cursor()
      cursor.execute("SELECT * FROM warnings WHERE user = ? AND guild = ?", (member.id, ctx.guild.id))
      data = cursor.fetchall() 
      if len(data) >= 3:
            muteRole =  discord.utils.get(ctx.guild.roles, name="Muted")
            await member.add_roles(muteRole)
            await ctx.send (f"You have been warned {len(data)} time and you are now temp muted")
            await asyncio.sleep(3600)
            await member.remove_roles(muteRole)
            await ctx.send (f"{member.mention} You have been unmuted")

            db = sqlite3.connect("warning.sqlite")
      cursor =db.cursor()
      cursor.execute("SELECT * FROM warnings WHERE user = ? AND guild = ?", (member.id, ctx.guild.id))
      data = cursor.fetchall() 
      if len(data) >= 4:
            muteRole =  discord.utils.get(ctx.guild.roles, name="Muted")
            await member.add_roles(muteRole)
            await ctx.send (f"You have been warned {len(data)} time and you are now temp muted")
            await asyncio.sleep(345600)
            await member.remove_roles(muteRole)
            await ctx.send (f"{member.mention} You have been unmuted")
            
            db = sqlite3.connect("warning.sqlite")
      cursor =db.cursor()
      cursor.execute("SELECT * FROM warnings WHERE user = ? AND guild = ?", (member.id, ctx.guild.id))
      data = cursor.fetchall() 
      if len(data) >= 5:
            muteRole =  discord.utils.get(ctx.guild.roles, name="Muted")
            await member.add_roles(muteRole)
            await ctx.send (f"You have been warned {len(data)} time and you are now temp muted")
            await asyncio.sleep(604800)
            await member.remove_roles(muteRole)
            await ctx.send (f"{member.mention} You have been unmuted")

            db = sqlite3.connect("warning.sqlite")
      cursor =db.cursor()
      cursor.execute("SELECT * FROM warnings WHERE user = ? AND guild = ?", (member.id, ctx.guild.id))
      data = cursor.fetchall() 
      if len(data) >= 6:
           ban = member 



@bot.command()
async def removewarn(ctx, member:discord.Member):
      db = sqlite3.connect("warning.sqlite")
      cursor =db.cursor()
      cursor.execute("SELECT reason FROM warnings WHERE user = ? AND guild = ?", (member.id, ctx.guild.id))
      data = cursor.fetchone()
      if data:
           cursor.execute("DELETE FROM warnings WHERE user = ? AND guild = ?", (member.id, ctx.guild.id))
           await ctx.send("Warning has benn removed")
      else:
           await ctx.send("You don't have any warnings")

           db.commit()