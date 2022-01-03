import discord
from discord.ext import commands

class Balance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["bal", "creds", "coins" "pokecoins", "gems", "credits"])
    async def balance(self, ctx):
        member = ctx.author.id

    # avatar = ctx.author.avatar_url
        embed = discord.Embed(
        title=f"Your Balance",
        description="")
    # embed.set_thumbnail(url=avatar)
        embed.add_field(name="Pokecoins", value=f"0")
        embed.add_field(name="Gems", value=f"None")
        embed.color=0x00ffff
        await ctx.reply(embed=embed, mention_author=False)

def setup(bot):
    bot.add_cog(Balance(bot))