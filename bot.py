import discord
import json
import asyncio
import requests
import feedparser
import os
import ssl

from discord.ext import commands, tasks
from sos import bigsos
from sos import smsos
from sos import NEWMOHW
from logger import logger3

intents = discord.Intents.all()

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

prefix = 'q/'
class sosCommand( commands.DefaultHelpCommand ):
  def __init__( self,**options ):
    super().__init__( **options )
    self.command_attrs["name"] = "sos"

bot = commands.Bot(command_prefix=prefix, help_command = sosCommand(), intents=intents, owner_ids="593666614717841419")

@tasks.loop(seconds=1)
async def status_task():
    await bot.change_presence(status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.watching, name=F"{prefix}help"))
    await asyncio.sleep(5)
    await bot.change_presence(status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.watching, name="堅果真好吃OwO"))
    await asyncio.sleep(5)
    await bot.change_presence(status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.watching,name=f'我正在 {(str(len(bot.guilds)))}' + "個伺服器做奴隸"))
    await asyncio.sleep(5)

@tasks.loop(minutes=1)
async def sosup():
    ssl._create_default_https_context = ssl._create_unverified_context
    with open('time.json', mode='r', encoding='UTF8') as jfile:
        svset = json.load(jfile)
    tokenAPI = jdata["APITOKEN"]
    API = f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization={tokenAPI}"  # 大型地震
    API2 = f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization={tokenAPI}"  # 小型地震
    MOHW = f"https://www.mohw.gov.tw/rss-16-1.html"  # 衛福部

    eew = (requests.get(API)).json()
    eew2 = (requests.get(API2)).json()
    cov = feedparser.parse(MOHW)

    originTime = eew['records']['earthquake'][0]["earthquakeInfo"]["originTime"]  # 大型地震發生時間
    originTime2 = eew2["records"]["earthquake"][0]["earthquakeInfo"]["originTime"]  # 小型地震發生時間
    newsID = cov["entries"][0]['newsid']

    site = ['BIGSOS'] + ['SMSOS'] + ['NEWMOHW']

    for i in range(len(site)):
        if site[i] not in svset:
            svset[site[i]] = ""
            print("建立網址紀錄")
    for i in range(len(site)):
        if site[i] == 'BIGSOS':
            if originTime != svset[site[i]]:
                channel = bot.get_channel(808976066353037364)
                svset[site[i]] = originTime
                await bigsos(channel)
                with open('time.json', 'w', encoding='UTF8') as outfile:
                    json.dump(svset, outfile, ensure_ascii=False, indent=4)
        if site[i] == 'SMSOS':
            if originTime2 != svset[site[i]]:
                channel = bot.get_channel(808976066353037364)
                svset[site[i]] = originTime2
                await smsos(channel)
                with open('time.json', 'w', encoding='UTF8') as outfile:
                    json.dump(svset, outfile, ensure_ascii=False, indent=4)
        if site[i] == 'NEWMOHW':
            if newsID not in svset[site[i]]:
                channel = bot.get_channel(808976066353037364)
                svset[site[i]].append(newsID)
                await NEWMOHW(channel, MOHW)
                with open('time.json', 'w', encoding='UTF8') as outfile:
                    json.dump(svset, outfile, ensure_ascii=False, indent=4)

@tasks.loop(hours=1)
async def test():
    message_channel = bot.get_channel(808976065984200732)
    await message_channel.send("`TESTRRR 1HOURS`")

@bot.event
async def on_ready():
    await logger3('discord', "-"*10)
    await logger3('discord', "bot Loading...")
    sosup.start()
    #test.start()
    status_task.start()
    print(">> Bot is online <<")
    print(bot.user.name)
    print(bot.user.id)
    print(f'prefix:{prefix}')
    print(str(len(bot.guilds)) + " servers")
    print('========OwO========')
    await logger3('discord', ">> Bot is online <<")
    # ------------------------------------------------------------------------------------------------------------------

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
