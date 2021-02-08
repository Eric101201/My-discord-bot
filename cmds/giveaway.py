import discord
import asyncio
import random

import datetime
from discord.ext import commands

prefix = 'w+'

def convert(time):
    pos = ["s", "m", "h", "d"]

    time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d" : 3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]

class giveaway(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_guild_permissions(administrator=True)
    @commands.command(name='gstart', help='抽獎系統 <抽獎倒數時間> <數量> <抽獎內容>')
    async def gstart(self, ctx, mins, num:int, *, prize:str):
        await ctx.message.delete()
        nowtime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
        time2 = convert(mins)

        embed = discord.Embed(title='抽獎系統!', color=discord.Colour.orange())
        embed.add_field(name='抽獎獎品:', value=f'`{prize}`', inline=False)
        embed.add_field(name='開始時間:', value=f'{nowtime}', inline=False)
        embed.set_footer(text=f'結束於 {mins} 後')

        my_msg = await ctx.send(embed=embed)

        await my_msg.add_reaction("🎉")

        await asyncio.sleep(time2)

        new_msg = await ctx.channel.fetch_message(my_msg.id)

        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))
        embed2 = discord.Embed(title='恭喜中獎者', color=discord.Colour.red())
        embed2.add_field(name='抽獎獎品:', value=f'`{prize}`', inline=False)
        online=[]
        for member in users:
            online.append(member.id)
        random_online = random.sample(online, k=num)
        for squad in range(1):
            a = random.sample(random_online, k=num)
            for i in a:
                await ctx.send(f'<@{i}>')
                embed2.add_field(name=f'中獎者:', value=f'<@{i}>', inline=True)
            for name in a:
                random_online.remove(name)

        embed2.add_field(name='訊息連結:', value=f'[點此傳送!!]({my_msg.jump_url})', inline=False)
        await ctx.send(embed=embed2)
        await ctx.send("================================")

def setup(bot):
    bot.add_cog(giveaway(bot))