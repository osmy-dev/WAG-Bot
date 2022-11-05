import discord
from discord.ext import commands
import datetime
import os

bot = commands.Bot(command_prefix='o?', intents=discord.Intents.all())

@bot.event
async def on_ready():
  print("OceanBot - WAG")
  print("This Bot Made By OsmyTeam")
  print("Enabing System...")
  print("----------")
  await bot.change_presence(activity=discord.Game("OsmyNetwork"))

@bot.event
async def on_member_join(member):
  channel = bot.get_channel() #channel id
  
  await channel.send(f"{member.mention} 欢迎来到OsmyNetwork!")

@bot.event
async def on_member_remove(member):
  channel = bot.get_channel() #channel id
  await channel.send(f"{member.mention} 离开了OsmyNetwork")

bot.run("") #Bot Token
