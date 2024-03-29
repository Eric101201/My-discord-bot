import re
import discord
import feedparser
import requests
import datetime
import json
import asyncio
from pytz import timezone

with open('setting.json', 'r', encoding='utf8') as jfile:
  jdata = json.load(jfile)

async def bigsos(channel):
  tokenAPI = jdata["APITOKEN"]
  API = f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization={tokenAPI}"  # 大型地震
  r = requests.get(API)
  eew = r.json()
  inp = eew["records"]["earthquake"][0]
  owwww = inp["intensity"]["shakingArea"]
  shaking = []
  inpinfo = inp["earthquakeInfo"]
  helpawa = inp["web"]                                    #資料連結
  earthquakeNo = inp["earthquakeNo"]                      #幾號地震
  location = inpinfo["epiCenter"]["location"]             #發生地點
  originTime = inpinfo["originTime"]                      #發生時間
  magnitdueType = inpinfo["magnitude"]["magnitdueType"]   #規模單位
  magnitudeValue = inpinfo["magnitude"]["magnitudeValue"] #規模單位
  value = inpinfo["depth"]["value"]                       #地震深度
  unit = inpinfo["depth"]["unit"]                         #深度單位
  urlicon = inp["reportImageURI"]                         #深度單位
  embed = discord.Embed(title=eew['records']['datasetDescription'], color=0xff0000)
  embed.set_author(name="台灣地震報告系統", icon_url='https://media.discordapp.net/attachments/345147297539162115/732527807435112478/EEW.png')
  embed.add_field(name="報告連結", value=f"[中央氣象局]({helpawa})", inline=True)  #報告連結
  embed.add_field(name="編號", value=f"{earthquakeNo}", inline=True)              #編號
  embed.add_field(name="震央位置", value=f"{location}", inline=True)              #震央位置
  embed.add_field(name="發生時間", value=f"{originTime}", inline=True)            #發生時間
  embed.add_field(name=f"{magnitdueType}", value=f"{magnitudeValue}", inline=True) #規模
  embed.add_field(name="深度", value=f"{value}{unit}", inline=True)               #發生時間
  embed.set_image(url=f"{urlicon}")
  for i in owwww:
    if '最' in i['areaDesc']:
      shaking.append({'desc': i['areaDesc'], 'name': i['areaName']})
  shaking.sort(key=lambda i: i['desc'])  # 以 shaking[i]['desc'] 的字母 a ~ z 排序
  for i in shaking:
    embed.add_field(name=i['desc'], value=i['name'], inline=False)
  embed.set_footer(text="地震報告提供", icon_url='https://media.discordapp.net/attachments/345147297539162115/732527875839885312/ROC_CWB.png')
  await channel.send(embed=embed)

async def smsos(channel):
  tokenAPI = jdata["APITOKEN"]
  API2 = f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization={tokenAPI}"  # 小型地震
  r = requests.get(API2)
  eew = r.json()
  inp = eew["records"]["earthquake"][0]
  owwww = inp["intensity"]["shakingArea"]
  shaking = []
  inpinfo = inp["earthquakeInfo"]
  helpawa = inp["web"]                                    #資料連結
  earthquakeNo = inp["earthquakeNo"]                      #幾號地震
  location = inpinfo["epiCenter"]["location"]             #發生地點
  originTime = inpinfo["originTime"]                      #發生時間
  magnitdueType = inpinfo["magnitude"]["magnitdueType"]   #規模單位
  magnitudeValue = inpinfo["magnitude"]["magnitudeValue"] #規模單位
  value = inpinfo["depth"]["value"]                       #地震深度
  unit = inpinfo["depth"]["unit"]                         #深度單位
  urlicon = inp["reportImageURI"]                         #深度單位
  embed = discord.Embed(title=eew['records']['datasetDescription'], color=0xff0000)
  embed.set_author(name="台灣地震報告系統", icon_url='https://media.discordapp.net/attachments/345147297539162115/732527807435112478/EEW.png')
  embed.add_field(name="報告連結", value=f"[中央氣象局]({helpawa})", inline=True)  #報告連結
  embed.add_field(name="編號", value=f"{earthquakeNo}", inline=True)              #編號
  embed.add_field(name="震央位置", value=f"{location}", inline=True)              #震央位置
  embed.add_field(name="發生時間", value=f"{originTime}", inline=True)            #發生時間
  embed.add_field(name=f"{magnitdueType}", value=f"{magnitudeValue}", inline=True) #規模
  embed.add_field(name="深度", value=f"{value}{unit}", inline=True)               #發生時間
  embed.set_image(url=f"{urlicon}")
  for i in owwww:
    if '最' in i['areaDesc']:
      shaking.append({'desc': i['areaDesc'], 'name': i['areaName']})
  shaking.sort(key=lambda i: i['desc'])  # 以 shaking[i]['desc'] 的字母 a ~ z 排序
  for i in shaking:
    embed.add_field(name=i['desc'], value=i['name'], inline=False)
  embed.set_footer(text="地震報告提供", icon_url='https://media.discordapp.net/attachments/345147297539162115/732527875839885312/ROC_CWB.png')
  await channel.send(embed=embed)

async def NEWMOHW(channel, url):
  rss = feedparser.parse(url)
  oaoa = rss['entries'][0]['title']
  owow = rss.entries[0]['summary']
  link = rss.entries[0]['link']
  covtime = rss["entries"][0]["published"]
  text = re.sub("<.*?>", "", owow)
  text1 = re.sub("&nbsp;", "", text)
  text2= '%.800s' % text1
  if len(text2) == 800:
    text3 = f'{text2}　　....([詳細內容請點擊此處觀看]({link}))'
  else:
    text3 = text2
  tz = timezone('Asia/Taipei')
  nowtime = datetime.datetime.now(tz).strftime("%Y/%m/%d %H:%M")
  embed = discord.Embed(title=f'{oaoa}', color=discord.Colour.blue())
  embed.set_author(name='衛生福利部公告',
                    icon_url='https://images-ext-1.discordapp.net/external/xrfvu0X7I_vcTEmPlp0x5JqmlM9D17azlTEbYTOVFlM/https/upload.wikimedia.org/wikipedia/commons/thumb/a/a3/ROC_Ministry_of_Health_and_Welfare_Seal.svg/1200px-ROC_Ministry_of_Health_and_Welfare_Seal.svg.png?width=677&height=677')
  embed.add_field(name='新聞連結', value=f'[點擊此處]({link})', inline=True)
  embed.add_field(name='發布時間', value=f'{covtime}', inline=True)
  embed.add_field(name='內容', value=f'{text3}', inline=False)
  embed.set_footer(text=f'衛生福利部RSS服務提供• {nowtime} ',
                    icon_url='https://images-ext-1.discordapp.net/external/xrfvu0X7I_vcTEmPlp0x5JqmlM9D17azlTEbYTOVFlM/https/upload.wikimedia.org/wikipedia/commons/thumb/a/a3/ROC_Ministry_of_Health_and_Welfare_Seal.svg/1200px-ROC_Ministry_of_Health_and_Welfare_Seal.svg.png?width=677&height=677')
  await channel.send(embed=embed)