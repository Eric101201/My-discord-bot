import discord
import time, os, psutil

from datetime import datetime
from discord.ext import commands

prefix = 'w+'

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        t1 = time.perf_counter()
        await ctx.trigger_typing()
        t2 = time.perf_counter()
        await ctx.trigger_typing()
        nowtime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

        embed=discord.Embed(title="延遲(PING)", color=ctx.author.colour)
        process = psutil.Process(os.getpid()).memory_info().rss # get app used ram
        percent = psutil.virtual_memory().percent # get used ram percent
        embed.add_field(name="Used Ram", value=f"```{round(process/1000000)} MB ({percent}%)```", inline=False)
        embed.add_field(name="Bot Ping", value=f"```{round(self.bot.latency*1000)} ms```", inline=True)
        embed.add_field(name="Sys Ping", value=f"```{round((t2-t1)*1000)} ms```", inline=True)
        embed.set_footer(text=f"👾{nowtime}")
        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(ping(bot))