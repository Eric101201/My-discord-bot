import discord
import json
import time
import random
import psutil
import platform

from random import randint
from discord.ext import commands
from datetime import datetime

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 1

async def add_experience(users, user, exp):
    users[f'{user.id}']['experience'] += int(exp)

async def level_up(users, user, message):
    with open('users.json', 'r') as g:
        levels = json.load(g)

    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(experience ** (1 / 4))
    if lvl_start < experience ** (1 / 4):
        #embed = discord.Embed(title=f'{user}恭喜你 你的等級到了 {lvl_end} 繼續加油<3', description='可輸入"w+level" 來查詢自己的等級喔<3', color=discord.colour.Color.orange())

        #await message.channel.send(embed=embed)
        users[f'{user.id}']['level'] = lvl_end
        return int(experience ** (1/4))
    return int(experience ** (1/4))

class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):

        with open('users.json', 'r') as f:
            users = json.load(f)

        await update_data(users, member)

        with open('users.json', 'w') as f:
            json.dump(users, f, ensure_ascii=False, indent=4)

        channel = self.bot.get_channel(int(jdata['Join_channel']))

        _weekday = {
            0: '星期一',
            1: '星期二',
            2: '星期三',
            3: '星期四',
            4: '星期五',
            5: '星期六',
            6: '星期日'
        }

        #格林威治天文臺時間
        t = time.gmtime(time.time())

        #月份天數陣列
        day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        #轉成代數
        y = t.tm_year
        M = t.tm_mon
        d = t.tm_mday
        h = t.tm_hour + 8
        m = t.tm_min
        s = t.tm_sec

        #判斷潤平年
        if y % 400 == 0:
            day[2] = 29
        elif y % 100 == 0:
            day[2] = 28
        elif y % 4 == 0:
            day[2] = 29
        else:
            day[2] = 28

#處裡跨月跨年狀況
        d = d + int(h / 24)
        h = h % 24
        tm = day[M]
        M = M + int(d / tm)
        d = d % tm
        y = y + int(M / 12)
        M = M % 12

        #s 秒
        #m 分
        #h 時
        #d 日
        #M 月
        #y 年

        g = (_weekday[datetime.today().weekday()])
        txt = "{}:{}:{}"
        txt2 = "{}年{}月{}日 {}"
        print(f"歡迎加入{member}您加入時間: \n" + txt.format(h, m, s) + "/" +
              txt2.format(y, M, d, g))

        embed = discord.Embed(
            title="", description="", color=(random.choice(jdata['顏色'])))
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_author(
            name="OwO Bot",
            url="https://discord.gg/nRa2994",
            icon_url=
            "https://images-ext-1.discordapp.net/external/x7kxTszr-e7WXPCkD11lhepLD457nLcMleTA4B1t8kM/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/636559032324325417/280943367acac65988c95de80ef5a1e2.webp?width=677&height=677"
        )
        embed.add_field(
            name='歡迎加入同樂群組',
            value='歡迎您加入同樂群組,跟我們大家一起玩OwO!\n\n'
            f':woman_raising_hand:加入成員名稱:  {member.mention}\n:clock3:加入時間: ' +
            txt.format(h, m, s) + "\n" + ':calendar_spiral: 加入日期: ' +
            txt2.format(y, M, d, g),
            inline=False)

        embed.set_footer(text=(random.choice(jdata['加入aaa'])))
        await channel.send(member.mention, embed=embed)
        role = discord.utils.get(member.guild.roles, name="Player")
        await member.add_roles(role)
        print(f"歡迎加入{member} 已給予:{role}身分組  您加入時間: \n" + "加入時間: " +
              txt.format(h, m, s) + "/" + txt2.format(y, M, d, g))

    @commands.Cog.listener()
    async def on_member_remove(self, member):

        with open('users.json', 'r') as f:
            users = json.load(f)

        users.pop(str(member.id))

        with open('users.json', 'w') as f:
            json.dump(users, f, ensure_ascii=False, indent=4)

        channel = self.bot.get_channel(int(jdata['Leave_channel']))

        _weekday = {
            0: '星期一',
            1: '星期二',
            2: '星期三',
            3: '星期四',
            4: '星期五',
            5: '星期六',
            6: '星期日'
        }

        #格林威治天文臺時間
        t = time.gmtime(time.time())

        #月份天數陣列
        day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        #轉成代數
        y = t.tm_year
        M = t.tm_mon
        d = t.tm_mday
        h = t.tm_hour + 8
        m = t.tm_min
        s = t.tm_sec

        #判斷潤平年
        if y % 400 == 0:
            day[2] = 29
        elif y % 100 == 0:
            day[2] = 28
        elif y % 4 == 0:
            day[2] = 29
        else:
            day[2] = 28


#處裡跨月跨年狀況
        d = d + int(h / 24)
        h = h % 24
        tm = day[M]
        M = M + int(d / tm)
        d = d % tm
        y = y + int(M / 12)
        M = M % 12

        #s 秒
        #m 分
        #h 時
        #d 日
        #M 月
        #y 年

        g = (_weekday[datetime.today().weekday()])
        txt = "{} {}:{}"
        txt2 = "{}年{}月{}日 {}"
        print(f"{member} 退出伺服器 " + txt.format(h, m, s) + "/" +
              txt2.format(y, M, d, g))

        embed1 = discord.Embed(
            title="", description="", color=(random.choice(jdata['顏色'])))
        embed1.set_thumbnail(url=member.avatar_url)
        embed1.set_author(
            name="OwO Bot",
            url="https://discord.gg/nRa2994",
            icon_url=
            "https://images-ext-1.discordapp.net/external/x7kxTszr-e7WXPCkD11lhepLD457nLcMleTA4B1t8kM/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/636559032324325417/280943367acac65988c95de80ef5a1e2.webp?width=677&height=677"
        )
        embed1.add_field(
            name='QAQ',
            value='\n\n'
            f'{member.mention}退出同樂了:tired_face:....\n:clock3:退出時間: ' +
            txt.format(h, m, s) + "\n" + ':calendar_spiral:退出日期: ' +
            txt2.format(y, M, d, g),
            inline=False)

        embed1.set_footer(
            text=(random.choice(jdata['加入aaa'])),
        )
        await channel.send(embed=embed1)

    @commands.Cog.listener()
    async def on_message(self, msg):

        if msg.author.bot == False:
            with open('users.json', 'r') as f:
                users = json.load(f)

            await update_data(users, msg.author)
            await add_experience(users, msg.author, randint(1, 5)) #random.choice(owww)
            await level_up(users, msg.author, msg)

            with open('users.json', 'w') as f:
                json.dump(users, f, ensure_ascii=False, indent=4)

        if msg.content.lower().startswith(
                '蹦假崩') and msg.author != self.bot.user:
            await msg.delete()
            await msg.channel.send('**蹦蹦告訴本鼠他要去吃飯**')

        if msg.content.lower().startswith(
                '綠露營') and msg.author != self.bot.user:
            await msg.delete()
            await msg.channel.send('**伊綠告訴本鼠連假要去露營**')

        if msg.content.lower().startswith(
                '蹦豬') and msg.author != self.bot.user:
            await msg.delete()
            await msg.channel.send('**蹦蹦告訴本鼠他要去睡覺了！**')

        if msg.content.lower().startswith(
                '/狀態') and msg.author != self.bot.user:
            cpufreq = psutil.cpu_freq()
            svmem = psutil.virtual_memory()
            uname = platform.uname()

            guild = msg.guild
            embed = discord.Embed()
            # embed.set_thumbnail(url=guild.icon_url)
            embed.set_author(name=guild.name, icon_url=guild.icon_url)
            embed.add_field(name="CPU名稱", value=f"{uname.processor}", inline=True)
            embed.add_field(name="CPU使用量", value=f"`{psutil.cpu_percent(percpu=False, interval=1)}%`", inline=True)

            embed.add_field(name="電腦平台", value=f"{uname.system} {uname.release}", inline=False)

            embed.add_field(name="RAM總大小", value=f"`{get_size(svmem.total)}`", inline=True)
            embed.add_field(name="RAM剩餘大小", value=f"`{get_size(svmem.available)}`", inline=True)
            embed.add_field(name="RAM使用大小", value=f"`{get_size(svmem.used)}`", inline=True)
            embed.add_field(name="RAM使用量", value=f"`{svmem.percent}%`", inline=True)

            embed.set_footer(text="製作by.Eric/伊綠")
            await msg.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Event(bot))
