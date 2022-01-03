import discord
from discord.ext import commands
from config import DEFAULT_PREFIX

class Shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot








    @commands.command()
    async def shop(self, ctx, *, page: int = 0):
        if page == 0:
            botname = self.bot.user.name
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

        elif page == 1:
            embed = discord.Embed(
            title=f"XP Boosters and Rare Candies",
            description=f"Get into your desired shop by using the `{DEFAULT_PREFIX}shop <number>` command and buy items for your Pokemon!"
                )
            embed.add_field(name="2X Multiplier For 30 Minutes", value=f"> 200 Pokecoins\n`{DEFAULT_PREFIX}buy xp booster 1`")
            embed.add_field(name="2X Multiplier For 1 Hour", value=f"\n`{DEFAULT_PREFIX}buy xp booster 2`")
            embed.add_field(name="2X Multiplier For 2 Hours", value=f"\n`{DEFAULT_PREFIX}buy xp booster 3`")
            embed.add_field(name="4X Multiplier For 30 Minutes", value=f"\n`{DEFAULT_PREFIX}buy xp booster 4`")
            embed.add_field(name="Rare Candies", value=f"Rare candies level up your selected pokémon by one level for each candy you feed it\nfidsbvjbskvsd")
            embed.color=0x00ffff
            await ctx.reply(embed=embed, mention_author=False)

        else:
            pass

def setup(bot):
    bot.add_cog(Shop(bot))