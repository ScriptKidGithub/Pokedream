import discord
from discord.ext import commands
from config import DEFAULT_PREFIX, ADMIN_LOGS, BOT_ADMIN

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def admin(self, ctx):
        await ctx.send(f"Run `{DEFAULT_PREFIX}help admin` to view a list of all Admin commands!")

    @admin.command(name="addcoins")
    async def pokemonadd_admin(self, ctx, member: discord.Member, amount: int):
        if ctx.message.author.id == BOT_ADMIN:
            await ctx.send("You must own this bot to use Admin Commands!") # Checks if the user is a bot admin xd
        else:
            adminlog = self.bot.get_channel(ADMIN_LOGS)
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

def setup(bot):
    bot.add_cog(Admin(bot))