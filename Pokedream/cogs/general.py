import discord
from discord.ext import commands
from config import INVITE_LINK, SUPPORT_SERVER
import datetime
import time
import aiohttp
import asyncio
import random

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# TO-DO - FIX UPTIME ERRORS IN UPTIME AND STAT COMMANDS |||||||| IMPORT TIME AND USE IT 

#    start_time = datetime.time() 
#    @commands.command(aliases=["up"])
#    async def uptime(self, ctx):
#        current_time = datetime.time()
#        difference = int(round(current_time - start_time))
#        uptime = str(datetime.timedelta(seconds=difference))
#        await ctx.send(uptime)

#    start_time = datetime.time() 
    @commands.command(aliases=["botstats", "stats"])
    async def botinfo(self, ctx):
#       current_time = datetime.time()
#        difference = int(round(current_time - start_time))
#        uptime = str(datetime.timedelta(seconds=difference))
        botname = self.bot.user.name
        embed = discord.Embed(
        title=f"{botname} Statistics",
        description=f"[Support Server]({SUPPORT_SERVER}) | [Invite Me]({INVITE_LINK})")
        embed.add_field(name="Developers", value=f"None")    #embed.set_thumbnail(url=ctx.me.avatar.url)
        embed.add_field(name="Trainers", value=f"unknown")
        embed.add_field(name="Pokemon", value=f"unknown", inline=True)
        embed.add_field(name="Guilds", value=f"{len(ctx.bot.guilds):,}", inline=True)
#        embed.add_field(name="Uptime", value=f"{uptime}") 
        embed.add_field(name="Websocket", value=f"{round((self.bot.latency)*1000)} ms")   
        embed.color=0x00ffff               
        await ctx.reply(embed=embed, mention_author=False) 

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(
            title=f"{self.bot.user.name} Links", 
            description="")
        embed.add_field(name="Invite Bot", value=f"{INVITE_LINK}")
        embed.add_field(name="Support Server", value=f"{SUPPORT_SERVER}")
        embed.add_field(name="Vote", value=f"Not Available")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(General(bot))