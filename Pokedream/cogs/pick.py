import discord
from discord.ext import commands
from config import DEFAULT_PREFIX
from starters import STARTERS

class Pick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pick(self, ctx, message):
        if message in STARTERS:
            await ctx.send(f"Congratulations {ctx.author.mention} You have picked {message} as your starter Pokemon! Run `{DEFAULT_PREFIX}info` to view the statistics of the Starter!")
        else:
            await ctx.send(f"That is not a valid starter pokemon!")

def setup(bot):
    bot.add_cog(Pick(bot))