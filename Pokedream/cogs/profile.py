import discord
from discord.ext import commands

class Profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def profile(self, ctx):
        botname = self.bot.user.name
        embed = discord.Embed(
        title=f"Your Game Profile",
        description=f"...ok"
        )
        embed.color=0x00ffff
        await ctx.reply(embed=embed, mention_author=False)

def setup(bot):
    bot.add_cog(Profile(bot))