import discord

from discord.ext import commands

class vote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_guild_permissions(administrator=True)
    @commands.command(name='vote', help='投票功能 <主題> <選項1> <選項2>')
    async def vote(self, ctx, title, list_1, list_2):
        await ctx.send(f'📝{title}')
        embed=discord.Embed(title=f'{title}', description="", color=0x15caea)
        embed.add_field(name="1️⃣", value=f'{list_1}', inline=False)
        embed.add_field(name="2️⃣", value=f'{list_2}', inline=False)

        msg = await ctx.send(embed=embed)
        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")

def setup(bot):
    bot.add_cog(vote(bot))
