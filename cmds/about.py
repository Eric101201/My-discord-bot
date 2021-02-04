import discord
from discord.ext import commands
import json
import psutil
import platform

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='info', help='機器人狀態')
    async def info(self, ctx):
        svmem = psutil.virtual_memory()
        uname = platform.uname()
    
        guild = ctx.guild
        embed=discord.Embed(color=ctx.author.colour)
        #embed.set_thumbnail(url=guild.icon_url)
        embed.set_author(name=guild.name, icon_url=guild.icon_url)
        embed.add_field(name="CPU名稱",value=f"{uname.processor}",inline=True)
        embed.add_field(name="CPU使用量", value=f"`{psutil.cpu_percent(percpu=False, interval=1)}%`",inline=True)

        embed.add_field(name="電腦平台",value=f"{uname.system} {uname.release}",inline=False)
    
        embed.add_field(name="RAM總大小",value=f"`{get_size(svmem.total)}`",inline=True)
        embed.add_field(name="RAM剩餘大小",value=f"`{get_size(svmem.available)}`",inline=True)
        embed.add_field(name="RAM使用大小",value=f"`{get_size(svmem.used)}`",inline=True)
        embed.add_field(name="RAM使用量",value=f"`{svmem.percent}%`",inline=True)

        embed.set_footer(text="製作by.Eric/伊綠")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(About(bot))