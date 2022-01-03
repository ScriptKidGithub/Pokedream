import discord
from discord.ext import commands
from config import DEFAULT_PREFIX

class Startgame(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["startgame"])
    async def start(self, ctx):
        botname = self.bot.user.name
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

def setup(bot):
    bot.add_cog(Startgame(bot))


