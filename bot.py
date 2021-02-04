import discord
import json
import os
import asyncio
import requests
import feedparser
import re

from datetime import datetime
from discord.ext import commands
from bs4 import BeautifulSoup

intents = discord.Intents.all()

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

prefix = 'q/'
bot = commands.Bot(command_prefix=prefix, help_command=None, intents=intents, owner_ids="593666614717841419")

async def status_task():
    while True:
        await bot.change_presence(status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.watching, name=F"{prefix}help"))
        await asyncio.sleep(5)
        await bot.change_presence(status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.watching, name="堅果真好吃OwO"))
        await asyncio.sleep(5)
        await bot.change_presence(status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.watching,name=f'我正在 {(str(len(bot.guilds)))}' + "個伺服器做奴隸"))
        await asyncio.sleep(5)

async def OAO():
    while True:
        #地震
        inp = requests.get('https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization=CWB-731698FA-533A-4A00-A5BD-AA1C49EE1E80')
        sss = BeautifulSoup(inp.content, 'html.parser')
        eeee = json.loads(sss.text)
        originTime = eeee['records']['earthquake'][0]["earthquakeInfo"]["originTime"]  # 發生時間

        with open('data.json', 'r', encoding='utf8') as file2:
            jdata2 = json.load(file2)

        if originTime not in jdata2["Time1"]:
            helpawa = eeee['records']['earthquake'][0]['web']  # 資料連結
            earthquakeNo = eeee['records']['earthquake'][0]["earthquakeNo"]  # 幾號地震
            location = eeee['records']['earthquake'][0]["earthquakeInfo"]["epiCenter"]["location"]  # 發生地點
            originTime = eeee['records']['earthquake'][0]["earthquakeInfo"]["originTime"]  # 發生時間
            magnitdueType = eeee['records']['earthquake'][0]["earthquakeInfo"]["magnitude"]["magnitdueType"]  # 規模單位
            magnitudeValue = eeee['records']['earthquake'][0]["earthquakeInfo"]["magnitude"]["magnitudeValue"]  # 規模單位
            value = eeee['records']['earthquake'][0]["earthquakeInfo"]["depth"]["value"]  # 地震深度
            unit = eeee['records']['earthquake'][0]["earthquakeInfo"]["depth"]["unit"]  # 深度單位
            urlicon = eeee['records']['earthquake'][0]["reportImageURI"]  # 地震報告圖片

            channel = bot.get_channel(701779007980437826)

            nowtime = datetime.now().strftime("%Y/%m/%d %H:%M")

            embed = discord.Embed(title='地震報告', color=discord.Colour.red())
            embed.set_author(name='台灣地震報告系統',
                             icon_url='https://images-ext-2.discordapp.net/external/MGVCq5ZDjXyZaG2UE0ysew_6fI_Rhbi4ayrVCFROmS4/https/media.discordapp.net/attachments/345147297539162115/732527807435112478/EEW.png')

            embed.add_field(name=f'報告連結', value=f'[中央氣象局]({helpawa})', inline=True)
            embed.add_field(name='編號', value=earthquakeNo, inline=True)
            embed.add_field(name='震央位置', value=location, inline=True)
            embed.add_field(name='發生時間', value=originTime, inline=True)
            embed.add_field(name=magnitdueType, value=magnitudeValue, inline=True)
            embed.add_field(name='深度', value=f'{value}{unit}', inline=True)
            embed.set_image(url=urlicon)

            embed.set_footer(text=f'地震報告提供• {nowtime} ',
                             icon_url='https://images-ext-2.discordapp.net/external/OLPz8IZNv22U8L3ImuVy24c3nemqogFY7L1v9Y98z7s/https/media.discordapp.net/attachments/345147297539162115/732527875839885312/ROC_CWB.png')

            await channel.send(embed=embed)

            jdata2["Time1"] = originTime
            with open('data.json', 'w') as file2:
                json.dump(jdata2, file2)
        await asyncio.sleep(2)

        #小規模
        inp = requests.get('https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization=CWB-731698FA-533A-4A00-A5BD-AA1C49EE1E80')
        sss = BeautifulSoup(inp.content, 'html.parser')
        eeee = json.loads(sss.text)
        originTime2 = eeee['records']['earthquake'][0]["earthquakeInfo"]["originTime"]  # 發生時間

        with open('data.json', 'r', encoding='utf8') as file3:
            jdata3 = json.load(file3)

        if originTime2 not in jdata3["Time2"]:
            helpawa = eeee['records']['earthquake'][0]['web']  # 資料連結
            earthquakeNo = eeee['records']['earthquake'][0]["earthquakeNo"]  # 幾號地震
            location = eeee['records']['earthquake'][0]["earthquakeInfo"]["epiCenter"]["location"]  # 發生地點
            originTime2 = eeee['records']['earthquake'][0]["earthquakeInfo"]["originTime"]  # 發生時間
            magnitdueType = eeee['records']['earthquake'][0]["earthquakeInfo"]["magnitude"]["magnitdueType"]  # 規模單位
            magnitudeValue = eeee['records']['earthquake'][0]["earthquakeInfo"]["magnitude"]["magnitudeValue"]  # 規模單位
            value = eeee['records']['earthquake'][0]["earthquakeInfo"]["depth"]["value"]  # 地震深度
            unit = eeee['records']['earthquake'][0]["earthquakeInfo"]["depth"]["unit"]  # 深度單位
            urlicon = eeee['records']['earthquake'][0]["reportImageURI"]  # 地震報告圖片

            channel = bot.get_channel(701779007980437826)

            nowtime = datetime.now().strftime("%Y/%m/%d %H:%M")

            embed = discord.Embed(title='地震報告', color=discord.Colour.red())
            embed.set_author(name='台灣地震報告系統',
                             icon_url='https://images-ext-2.discordapp.net/external/MGVCq5ZDjXyZaG2UE0ysew_6fI_Rhbi4ayrVCFROmS4/https/media.discordapp.net/attachments/345147297539162115/732527807435112478/EEW.png')

            embed.add_field(name=f'報告連結', value=f'[中央氣象局]({helpawa})', inline=True)
            embed.add_field(name='編號', value='小規模地震無編號', inline=True)
            embed.add_field(name='震央位置', value=location, inline=True)
            embed.add_field(name='發生時間', value=originTime2, inline=True)
            embed.add_field(name=magnitdueType, value=magnitudeValue, inline=True)
            embed.add_field(name='深度', value=f'{value}{unit}', inline=True)
            embed.set_image(url=urlicon)

            embed.set_footer(text=f'地震報告提供• {nowtime} ',
                             icon_url='https://images-ext-2.discordapp.net/external/OLPz8IZNv22U8L3ImuVy24c3nemqogFY7L1v9Y98z7s/https/media.discordapp.net/attachments/345147297539162115/732527875839885312/ROC_CWB.png')
            await channel.send(embed=embed)
            jdata3["Time2"] = originTime2
            with open('data.json', 'w') as file3:
                json.dump(jdata3, file3)
        await asyncio.sleep(2)

        #肺炎
        rss_url = 'https://www.mohw.gov.tw/rss-16-1.html'
        rss = feedparser.parse(rss_url)
        link = rss.entries[0]['link']
        channel3 = bot.get_channel(701779007980437826)
        with open('data.json', 'r', encoding='utf8') as file4:
            jdata4 = json.load(file4)

        if link not in jdata4["link"]:
            rss_url = 'https://www.mohw.gov.tw/rss-16-1.html'
            rss = feedparser.parse(rss_url)
            oaoa = rss['entries'][0]['title']
            owow = rss.entries[0]['summary']
            link = rss.entries[0]['link']

            text = re.sub("<.*?>", "", owow)

            nowtime = datetime.now().strftime("%Y/%m/%d %H:%M")

            embed = discord.Embed(title=f'{oaoa}', color=discord.Colour.blue())
            embed.set_author(name='衛生福利部公告',
                             icon_url='https://images-ext-1.discordapp.net/external/xrfvu0X7I_vcTEmPlp0x5JqmlM9D17azlTEbYTOVFlM/https/upload.wikimedia.org/wikipedia/commons/thumb/a/a3/ROC_Ministry_of_Health_and_Welfare_Seal.svg/1200px-ROC_Ministry_of_Health_and_Welfare_Seal.svg.png?width=677&height=677')
            embed.add_field(name='新聞連結', value=f'[點擊此處]({link})', inline=False)
            embed.add_field(name='內容', value=f'{text}', inline=False)
            embed.set_footer(text=f'衛生福利部RSS服務提供• {nowtime} ',
                             icon_url='https://images-ext-1.discordapp.net/external/xrfvu0X7I_vcTEmPlp0x5JqmlM9D17azlTEbYTOVFlM/https/upload.wikimedia.org/wikipedia/commons/thumb/a/a3/ROC_Ministry_of_Health_and_Welfare_Seal.svg/1200px-ROC_Ministry_of_Health_and_Welfare_Seal.svg.png?width=677&height=677')

            await channel3.send(embed=embed)
            jdata4["link"] = link
            with open('data.json', 'w') as file4:
                json.dump(jdata4, file4)
        await asyncio.sleep(2)

@bot.event
async def on_ready():
    # channel = bot.get_channel(701779007980437826)
    bot.loop.create_task(status_task())
    bot.loop.create_task(OAO())
    # embed2=discord.Embed(title=">>Bot on ready<<", color=(random.choice(jdata['顏色'])))
    # await channel.send(embed=embed2)
    print(">> Bot is online <<")
    print(bot.user.name)
    print(bot.user.id)
    print(f'prefix:{prefix}')
    print(str(len(bot.guilds)) + " servers")
    print('========OwO========')

    # ------------------------------------------------------------------------------------------------------------------


for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
