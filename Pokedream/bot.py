import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from config import DEFAULT_PREFIX, BOT_TOKEN, STATUS_LOG, DEFAULT_PREFIX, OWNER_ID
import datetime
import os

bot = commands.Bot(command_prefix=commands.when_mentioned_or(DEFAULT_PREFIX),case_insensitive=True,owner_id=OWNER_ID,strip_after_prefix=True,intents=discord.Intents.all())
bot.load_extension("jishaku")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"📥 `cogs.{extension}`")

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"📤 `cogs.{extension}`")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event 
async def on_ready():
    status_channel = bot.get_channel(STATUS_LOG)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="p!help"))
    print(f"{bot.user.name} is online!") 
    await status_channel.send(f"`{datetime.datetime.now()}` | 🟡 Connected to Local Host `({round((bot.latency)*1000)} ms`)") 

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

bot.run(BOT_TOKEN)



