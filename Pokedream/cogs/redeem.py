import discord
from discord.ext import commands
from config import DEFAULT_PREFIX

class Redeem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def redeem(self, ctx):
        embed=discord.Embed(
            title="You have 0 Redeems",
            description="Redeem is a special type of Game Currency used for obtaining any catchable Pokemon of your choice! You can also use them to redeem Pokecoins!"
        )
        embed.add_field(name=f"{DEFAULT_PREFIX}redeem <pokemon>", value=f"Redeem a Pokemon directly to your Game Account")
        embed.add_field(name=f"{DEFAULT_PREFIX}redeem spawn <pokemon>", value=f"Redeem a Pokemon in this channel")
        embed.add_field(name=f"{DEFAULT_PREFIX}redeem coins", value=f"Redeems 15k Pokecoins")
        embed.color=0x00ffff
        await ctx.reply(embed=embed, mention_author=False)

def setup(bot):
    bot.add_cog(Redeem(bot))