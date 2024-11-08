import discord
from datetime import datetime

intents =discord.Intents.default()
intents.members = True
intents.messages = True

Wonderbot= discord.Bot(intents = intents) 

@Wonderbot.event
async def on_message_delete(message):
    z = Wonderbot.get.channel(1303980008179634207)
    embed = discord.embed(title= f"{message.author}'s Message was Deleted", description = f"Deleted Message: {message.content}\nAuthor: {message.author.mention}\nLocation: {message.channel.mention}", timestamp = datetime.now(), colour = discord.colour.red())
    embed.set_author(name = message.author.name, icon_url = message.author.display_avatar)
    await z.send(embed = embed)

@Wonderbot.event
async def on_message_edit(before, after):
     z = Wonderbot.get.channel(1303980008179634207)
    embed = discord.embed(title= f"{before.author} Edited Their Message", description = f"Before: {before.content}\nAfter: {after.content}\nAuthor: {message.author.mention}\nLocation: {before.channel.mention}", timestamp = datetime.now(), colour = discord.colour.blue())
    embed.set_author(name = after.name, icon_url = after.display_avatar)
    await z.send(embed = embed) 

@Wonderbot.event
async def on_membwe_update(before, after):
     z = Wonderbot.get.channel(1303980008179634207)
     if len(before.roles) > len(after.roles):
        role = next(role for role in before.roles if role not in after.roles)
        embed = discord.Embed(title = f"{before.author}'s Role has been Removed", description = f"{role.name} was removed from {before.author.mention}.", timestamp = datetime.now(), colour = discord.colour.red())
    elif len(after.roles) > len(before.roles):
role = next(role for role in after.roles if role not in before.roles)
embed = discord.Embed(title = f"{before.author} Got a New Role", description = f"{role.name} was added to {before.author.mention}.", timestamp = datetime.now(), colour = discord.colour.green())
elif before.nick != after.nick:
embed = discord.Embed(title = f"{before.author}'s Nickname Changed", description = f"Before: {before.nick}\nAfter: {after.nick}", timestamp = datetime.now(), colour = discord.colour.blue())
else:
return
    embed.set_author(name = after.name, icon_url = after.display_avatar)
    await z.send(embed = embed)

@Wonderbot.event
async def on_guild_channel_create(channel):
      z = Wonderbot.get.channel(1303980008179634207)
    embed = discord.embed(title= f"{channel.name} was Created", description = channel.mention, timestamp = datetime.now(), colour = discord.colour.green())
    await z.send(embed = embed)

@Wonderbot.event
async def on_guild_channel_delete(channel): 
    z = Wonderbot.get.channel(1303980008179634207)
    embed = discord.embed(title= f"{channel.name} was Deleted", timestamp = datetime.now(), colour = discord.colour.red())
    await z.send(embed = embed)