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
        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(color=0xFF0000)
            embed.add_field(name=F"**你似乎輸入了錯誤的指令，查看可用指令請使用 {prefix}help 指令**", value=f'```{error}```')

            await ctx.send(embed=embed)
            await asyncio.sleep(1)

        elif isinstance(error, commands.MissingRequiredArgument):
            embed2 = discord.Embed(color=0xFF0000)
            embed2.add_field(name=f"**Error! 您少輸入字串**", value=f'```{error}```')

            await ctx.send(embed=embed2)
            await asyncio.sleep(1)

def setup(bot):
    bot.add_cog(error(bot))