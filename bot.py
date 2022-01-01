import discord
from discord.ext import commands, tasks
from discord.ext.commands.core import bot_has_permissions
from discord.ext.commands.errors import BotMissingPermissions, CommandInvokeError, MissingPermissions, MissingRequiredArgument, MissingRole
from discord.ext.commands.help import DefaultHelpCommand
from discord.member import Member
from config import DEFAULT_PREFIX, BOT_TOKEN, EMOTE_INFO, STATUS_LOG, DEFAULT_PREFIX, OWNER_ID, ERROR_LOG, EMOTE_ERROR, EMOTE_SUCCESS, OWNER_ID, SUPPORT_SERVER, INVITE_LINK, EMBED_COLOR, BOT_ADMIN, DATABASE_URL, COLLECTION_NAME, CLUSTER_NAME, DATABASE_NAME, ADMIN_LOGS
import jishaku
from starters import STARTERS
import datetime
import aiohttp
import asyncio
import random
import time
from discord.ext.commands import CommandNotFound


bot = commands.Bot(command_prefix=commands.when_mentioned_or(DEFAULT_PREFIX),case_insensitive=True,owner_id=OWNER_ID,strip_after_prefix=True,intents=discord.Intents.all())

start_time = time.time() 
@bot.command(aliases=["up"])
async def uptime(ctx):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    uptime = str(datetime.timedelta(seconds=difference))
    await ctx.send(uptime)

start_time = time.time() 
@bot.command(aliases=["botstats", "stats"])
async def botinfo(ctx):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    uptime = str(datetime.timedelta(seconds=difference))
    botname = bot.user.name
    embed = discord.Embed(
    title=f"{botname} Statistics",
    description=f"[Support Server]({SUPPORT_SERVER}) | [Invite Me]({INVITE_LINK})")
    embed.add_field(name="Developers", value=f"None")    #embed.set_thumbnail(url=ctx.me.avatar.url)
    embed.add_field(name="Trainers", value=f"unknown")
    embed.add_field(name="Pokemon", value=f"unknown", inline=True)
    embed.add_field(name="Guilds", value=f"{len(ctx.bot.guilds):,}", inline=True)
    embed.add_field(name="Uptime", value=f"{uptime}") 
    embed.add_field(name="Websocket", value=f"{round((bot.latency)*1000)} ms")   
    embed.color=0x00ffff               
    await ctx.reply(embed=embed, mention_author=False) 

@bot.command()
async def invite(ctx):
    embed = discord.Embed(
        title=f"{bot.user.name} Links", 
        description="")
    embed.add_field(name="Invite Bot", value=f"{INVITE_LINK}")
    embed.add_field(name="Support Server", value=f"{SUPPORT_SERVER}")
    embed.add_field(name="Vote", value=f"Not Available")
    await ctx.send(embed=embed)


@bot.command(aliases=["startgame"])
async def start(ctx):
    botname = bot.user.name
    prefix = DEFAULT_PREFIX
    embed = discord.Embed(
    title=f"Welcome to the world of Pokemon!",
    description=f"Choose one of the starter pokemon with `{prefix}pick <pokemon>` command to start the Game!")
    embed.set_author(name=f"{botname}", url="", icon_url="")
    embed.add_field(name="Generation I (Kanto)", value=f"Bulbasaur | Charmander | Squirtle")
    embed.add_field(name="Generation II (Johto)", value=f"Chikorita | Cyndaquil | Totodile")
    embed.add_field(name="Generation III (Hoenn)", value=f"Treecko | Torchic | Mudkip")
    embed.add_field(name="Generation IV (Sinnoh)", value=f"Turtwig | Chimchar | Piplup")
    embed.add_field(name="Generation V (Unova)", value=f"Snivy | Tepig | Oshawott")
    embed.add_field(name="Generation VI (Kalos)", value=f"Chespin | Fennekin | Froakie")
    embed.add_field(name="Generation VII (Alola)", value=f"Rowlet | Litten | Popplio")
    embed.add_field(name="Generation VIII (Galar)", value=f"Grookey | Scorbunny | Sobble")
    embed.add_field(name="Generation IX (Hisui)", value=f"Unavailable")

    embed.color=0x00ffff
    await ctx.reply(embed=embed, mention_author=False)

@bot.command(aliases=["bal", "creds", "coins" "pokecoins", "gems", "credits"])
async def balance(ctx):
    member = ctx.author.id

   # avatar = ctx.author.avatar_url
    embed = discord.Embed(
    title=f"Your Balance",
    description="")
   # embed.set_thumbnail(url=avatar)
    embed.add_field(name="Pokecoins", value=f"{COLLECTION_NAME.findOne({'_id': ctx.author.id})['balance']}")
    embed.add_field(name="Gems", value=f"None")
    embed.color=0x00ffff
    await ctx.reply(embed=embed, mention_author=False)

@bot.command()
async def shop(ctx):
    botname = bot.user.name
    embed = discord.Embed(
    title=f"Welcome to {botname} shop!",
    description=f"Get into your desired shop by using the `{DEFAULT_PREFIX}shop <number>` command and buy items for your Pokemon!"
    )
    embed.add_field(name="XP Boosters and Candies", value=f"None")
    embed.add_field(name="Rare stones and Evolution Items", value=f"Get the list of items like stones and evolution items to evolve your Pokemon!")
    embed.add_field(name="Nature Modifiers", value=f"Get the list of items like nature modifiers to replace the nature of your Pokemon!")
    embed.add_field(name="Held Items", value=f"None")
    embed.add_field(name="Mega Stones and Evolutions", value=f"None")
    embed.add_field(name="Pokemon Forms", value=f"Get a list of forms which you can buy to evolve your Pokemon!")
    embed.add_field(name="Gmax Forms", value=f"None")
    embed.add_field(name="Gem Shop", value=f"None")
    embed.color=0x00ffff
    await ctx.reply(embed=embed, mention_author=False)

@bot.command()
async def profile(ctx):
    botname = bot.user.name
    embed = discord.Embed(
    title=f"Your Game Profile",
    description=f"...ok"
    )
    embed.color=0x00ffff
    await ctx.reply(embed=embed, mention_author=False)

@bot.command()
async def pick(ctx, message):
    if message in STARTERS:
        await ctx.send(f"Congratulations {ctx.author.mention} You have picked {message} as your starter Pokemon! Run `{DEFAULT_PREFIX}info` to view the statistics of the Starter!")
    else:
        await ctx.send(f"That is not a valid starter pokemon!")

@bot.command()
async def redeem(ctx):
    embed=discord.Embed(
        title="You have 0 Redeems",
        description="Redeem is a special type of Game Currency used for obtaining any catchable Pokemon of your choice! You can also use them to redeem Pokecoins!"
    )
    embed.add_field(name=f"{DEFAULT_PREFIX}redeem <pokemon>", value=f"Redeem a Pokemon directly to your Game Account")
    embed.add_field(name=f"{DEFAULT_PREFIX}redeem spawn <pokemon>", value=f"Redeem a Pokemon in this channel")
    embed.add_field(name=f"{DEFAULT_PREFIX}redeem coins", value=f"Redeems 15k Pokecoins")
    embed.color=0x00ffff
    await ctx.reply(embed=embed, mention_author=False)

@bot.group(invoke_without_command=True)
async def admin(ctx):
    await ctx.send(f"Run `{DEFAULT_PREFIX}help admin` to view a list of all Admin commands!")

@admin.command(name="addcoins")
async def pokemonadd_admin(ctx, member: discord.Member, amount: int):
    if ctx.message.author.id == BOT_ADMIN:
        await ctx.send("You must own this bot to use Admin Commands!")
    else:
        adminlog = bot.get_channel(ADMIN_LOGS)
        guildid = ctx.guild.id
        guildname = ctx.guild.name
        embed = discord.Embed(
            title="Admin command used",
            description=f"`{DEFAULT_PREFIX}admin addcoins`")
        embed.add_field(name=f"Responsible Admin", value=f"{ctx.author.name}")
        embed.add_field(name=f"User", value=f"{member.name} ({member.id})")
        embed.add_field(name=f"Amount", value=f"{amount}")
        embed.add_field(name=f"Guild", value=f"{guildname} ({guildid})")
        embed.color=0x00ffff
        await ctx.send(f"Added {amount} Pokecoins to {member.mention}")
        await adminlog.send(embed=embed)

bot.load_extension("jishaku")

@bot.event
async def on_ready():
    status_channel = bot.get_channel(STATUS_LOG)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="p!help"))
    print("Bot is online!")
    print(STARTERS)
    await status_channel.send(f"`{datetime.datetime.now()}` | 🟡 Reconnected to Local Host `({round((bot.latency)*1000)} ms`)")

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(ctx.command)
    raise error

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

bot.run(BOT_TOKEN)

#for filename in os.listdir("./cogs"):
 #   if filename.endswith("py"):
  #      bot.load_extension(f"cogs.{filename[:-3]}")
