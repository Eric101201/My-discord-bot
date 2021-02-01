import discord
import asyncio
import random
import time

from datetime import datetime
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
    @commands.command(name='gstart', help='抽獎系統 <抽獎倒數時間> <抽獎內容>')
    async def gstart(self, ctx, mins, *, prize:str):

        _weekday = {
            0: '星期一',
            1: '星期二',
            2: '星期三',
            3: '星期四',
            4: '星期五',
            5: '星期六',
            6: '星期日'
        }

        # 格林威治天文臺時間
        t = time.gmtime(time.time())

        # 月份天數陣列
        day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # 轉成代數
        y = t.tm_year
        M = t.tm_mon
        d = t.tm_mday
        h = t.tm_hour + 8
        m = t.tm_min
        s = t.tm_sec

        # 判斷潤平年
        if y % 400 == 0:
            day[2] = 29
        elif y % 100 == 0:
            day[2] = 28
        elif y % 4 == 0:
            day[2] = 29
        else:
            day[2] = 28

        # 處裡跨月跨年狀況
        d = d + int(h / 24)
        h = h % 24
        tm = day[M]
        M = M + int(d / tm)
        d = d % tm
        y = y + int(M / 12)
        M = M % 12

        # s 秒
        # m 分
        # h 時
        # d 日
        # M 月
        # y 年

        g = (_weekday[datetime.today().weekday()])
        txt = "{} {}:{}"
        txt2 = "{}/{}/{} {}"
        time2 = convert(mins)

        embed = discord.Embed(title='抽獎系統!', color=discord.Colour.orange())
        embed.add_field(name='抽獎獎品:', value=f'`{prize}`', inline=False)
        embed.add_field(name='開始時間:', value=txt2.format(y, M, d, g) + '-' + txt.format(h, m, s), inline=False)
        embed.set_footer(text=f'結束於 {mins} 後')

        my_msg = await ctx.send(embed=embed)

        await my_msg.add_reaction("🎉")

        await asyncio.sleep(time2)

        new_msg = await ctx.channel.fetch_message(my_msg.id)

        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))

        wimmer = random.choice(users)

        embed2 = discord.Embed(title='恭喜中獎者', color=discord.Colour.red())
        embed2.add_field(name=f'中獎者:', value=f'{wimmer.mention}', inline=True)
        embed2.add_field(name='抽獎獎品:', value=f'`{prize}`', inline=True)
        embed2.add_field(name='訊息連結:', value=f'[點此傳送!!]({my_msg.jump_url})', inline=False)

        await ctx.send(f'{wimmer.mention}')
        await ctx.send(embed=embed2)

def setup(bot):
    bot.add_cog(giveaway(bot))