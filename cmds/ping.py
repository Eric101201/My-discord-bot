import discord
import time, os, psutil

from pytz import timezone
from datetime import datetime
from discord.ext import commands

prefix = 'w+'

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping', help='機器人延遲')
    async def ping(self, ctx):
        tz = timezone('Asia/Taipei')
        t1 = time.perf_counter()
        await ctx.trigger_typing()
        t2 = time.perf_counter()
        await ctx.trigger_typing()
        nowtime = datetime.now(tz).strftime("%Y/%m/%d %H:%M:%S")
        svmem = psutil.virtual_memory()

        embed=discord.Embed(title="延遲(PING)", color=ctx.author.colour)
        embed.add_field(name="Used Ram", value=f"```{get_size(svmem.used)} ({svmem.percent}%)```", inline=False)
        embed.add_field(name="Bot Ping", value=f"```{round(self.bot.latency*1000)} ms```", inline=True)
        embed.add_field(name="Sys Ping", value=f"```{round((t2-t1)*1000)} ms```", inline=True)
        embed.set_footer(text=f"👾{nowtime}")
        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(ping(bot))