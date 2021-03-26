import discord
import json
import psutil
import platform
import datetime

from pytz import timezone
from random import randint
from discord.ext import commands
from discord import (
    Forbidden,
    HTTPException
)

from logger import msglog, log

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

auto_publish_channels = 809034639016460338, 809034393355157514

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

        await log('discord.event', f"{member} 加入 {member.guild.name}伺服器 id:{member.id}")

        channel = self.bot.get_channel(int(jdata['Join_channel']))
        tz = timezone('Asia/Taipei')
        nowtime = datetime.datetime.now(tz).strftime("%Y/%m/%d %H:%M:%S")
        embed = discord.Embed(
            title="", description="", color=discord.Color.blue())
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(
            name=f'歡迎加入{member.guild.name}',
            value=f'加入成員名稱:  {member.mention}\n加入時間: {nowtime}',
            inline=False)
        embed.add_field(name="伺服器人數：", value=f"{member.guild.member_count}", inline=False)
        await channel.send(member.mention, embed=embed)
        role = discord.utils.get(member.guild.roles, name="未驗證")
        await member.add_roles(role)


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        with open('users.json', 'r') as f:
            users = json.load(f)
        users.pop(str(member.id))
        with open('users.json', 'w') as f:
            json.dump(users, f, ensure_ascii=False, indent=4)

        await log('discord.event', f"{member} 退出 {member.guild.name}伺服器 id:{member.id}")

        channel = self.bot.get_channel(int(jdata['Leave_channel']))
        tz = timezone('Asia/Taipei')
        nowtime = datetime.datetime.now(tz).strftime("%Y/%m/%d %H:%M:%S")
        embed = discord.Embed(
            title="", description="", color=discord.Color.blue())
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(
            name='QAQ',
            value=f'**{member.name}退出了{member.guild.name}. \n退出時間: {nowtime}**.',
            inline=False)
        embed.add_field(name="伺服器人數：", value=f"{member.guild.member_count}", inline=False)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author.bot == False:
            try:
                await msglog('msglogger', f'{msg.guild.name} > {msg.author} > {msg.content}')
            except AttributeError:
                await msglog('私訊logger', f'{msg.author} > {msg.content}')

        if msg.author.bot == False:
            with open('users.json', 'r') as f:
                users = json.load(f)

            await update_data(users, msg.author)
            await add_experience(users, msg.author, randint(1, 5)) #random.choice(owww)
            await level_up(users, msg.author, msg)

            with open('users.json', 'w') as f:
                json.dump(users, f, ensure_ascii=False, indent=4)

        if msg.channel.id in auto_publish_channels:
            try:
                await msg.publish()
            except Forbidden as e:
                message_channel = self.bot.get_channel(808976065984200732)
                await message_channel.send(f'`{e.text}`\n請檢察頻道設定')
            except HTTPException as e:
                message_channel = self.bot.get_channel(808976065984200732)
                await message_channel.send(f'`{e.text}`')

        if msg.content.lower().startswith(
                '蹦假崩') and msg.author != self.bot.user:
            await msg.delete()
            await msg.channel.send('**蹦蹦告訴本鼠他要去吃飯**')

        if msg.content.lower().startswith(
                '綠露營') and msg.author != self.bot.user:
            await msg.delete()
            await msg.channel.send('**伊綠告訴本鼠連假要去露營**')

        if msg.content.lower().startswith(
                '阿蹦豬') and msg.author != self.bot.user:
            await msg.delete()
            await msg.channel.send('**蹦蹦告訴本鼠他要去睡覺了！**')

        if msg.content.lower().startswith(
                '/狀態') and msg.author != self.bot.user:
            cpufreq = psutil.cpu_freq()
            svmem = psutil.virtual_memory()
            uname = platform.uname()

            guild = msg.guild
            embed = discord.Embed()
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
