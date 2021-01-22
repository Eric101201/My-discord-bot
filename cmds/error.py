import discord
import json
import asyncio

from discord.ext import commands

prefix = 'w+'

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        embed = discord.Embed(title=F"你似乎輸入了錯誤的指令，查看可用指令請使用 {prefix} help 指令",
                              description=f"{error}",
                              color=ctx.author.colour)
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(embed=embed)
            await asyncio.sleep(1)

def setup(bot):
    bot.add_cog(error(bot))