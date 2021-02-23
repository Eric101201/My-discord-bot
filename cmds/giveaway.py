import discord
import asyncio
import random
import datetime
import json
from datetime import timedelta
from pytz import timezone
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

with open('giveaway/giveaway.json', mode='r', encoding='UTF8') as jfile:
    date = json.load(jfile)

class giveaway(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_guild_permissions(administrator=True)
    @commands.command(name='gstart', help='抽獎系統 <主題> <抽獎倒數時間> <數量> <抽獎內容>')
    async def gstart(self, ctx, name:str, mins, num:int, *, prize:str):

        tz = timezone('Asia/Taipei')
        time2 = convert(mins)
        nowtime = datetime.datetime.now(tz).strftime("%Y/%m/%d %H:%M:%S")
        endtime = datetime.datetime.now(tz)+timedelta(seconds=time2)
        endtime2 = endtime.strftime("%Y/%m/%d %H:%M:%S")

        embed = discord.Embed(title='抽獎系統!', color=discord.Colour.orange())
        embed.add_field(name='抽獎獎品:', value=f'`{prize}`', inline=True)
        embed.add_field(name='數量:', value=f'`{num}`', inline=False)
        embed.add_field(name='開始時間:', value=f'{nowtime}', inline=True)
        embed.add_field(name='結束時間:', value=f'{endtime2}', inline=True)
        embed.set_footer(text=f'發送訊息者:{ctx.author}')

        my_msg = await ctx.send(embed=embed)

        await my_msg.add_reaction("🎉")

        date[my_msg.id] = {}
        date[my_msg.id]['start_msg_id'] = str(my_msg.id)
        date[my_msg.id]['end_msg_id'] = ""
        date[my_msg.id]['channel_id'] = str(ctx.channel.id)
        date[my_msg.id]['title'] = name
        date[my_msg.id]['prize'] = prize
        date[my_msg.id]['Quantity'] = str(num)
        date[my_msg.id]['time'] = str(time2) + "s"
        date[my_msg.id]['start_time'] = nowtime
        date[my_msg.id]['end_time'] = endtime2
        date[my_msg.id]['all_user'] = []
        date[my_msg.id]['winnerid'] = []

        with open('giveaway/giveaway.json', 'w', encoding='UTF8') as f:
            json.dump(date, f, ensure_ascii=False, indent=4)

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

                date[my_msg.id]['winnerid'].append(i)
                with open('giveaway/giveaway.json', 'w', encoding='UTF8') as f:
                    json.dump(date, f, ensure_ascii=False, indent=4)

                embed2.add_field(name=f'中獎者:', value=f'<@{i}>', inline=True)
            for name in a:
                random_online.remove(name)

        embed2.add_field(name='訊息連結:', value=f'[點此傳送!!]({my_msg.jump_url})', inline=False)
        end_msg = await ctx.send(embed=embed2)

        for i in users:
            date[my_msg.id]['all_user'].append(i.id)

        date[my_msg.id]['end_msg_id'] = str(end_msg.id)
        with open('giveaway/giveaway.json', 'w', encoding='UTF8') as f:
            json.dump(date, f, ensure_ascii=False, indent=4)

        await ctx.send("================================")

def setup(bot):
    bot.add_cog(giveaway(bot))