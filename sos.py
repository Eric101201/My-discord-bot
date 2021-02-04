import json
import re
import discord
import feedparser
import requests
import datetime

async def bigsos(channel, API):
  r = requests.get(API)
  eew = r.json()
  inp = eew["records"]["earthquake"][0]
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
  embed.set_image(url=f"{urlicon}")
  embed.add_field(name="報告連結", value=f"[中央氣象局]({helpawa})", inline=True)  #報告連結
  embed.add_field(name="編號", value=f"{earthquakeNo}", inline=True)              #編號
  embed.add_field(name="震央位置", value=f"{location}", inline=True)              #震央位置
  embed.add_field(name="發生時間", value=f"{originTime}", inline=True)            #發生時間
  embed.add_field(name=f"{magnitdueType}", value=f"{magnitudeValue}", inline=True) #規模
  embed.add_field(name="深度", value=f"{value}{unit}", inline=True)               #發生時間
  embed.set_footer(text="地震報告提供", icon_url='https://media.discordapp.net/attachments/345147297539162115/732527875839885312/ROC_CWB.png')
  await channel.send(embed=embed)

async def smsos(channel, API2):
  r = requests.get(API2)
  eew = r.json()
  inp = eew["records"]["earthquake"][0]
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
  embed.set_image(url=f"{urlicon}")
  embed.add_field(name="報告連結", value=f"[中央氣象局]({helpawa})", inline=True)  #報告連結
  embed.add_field(name="編號", value=f"{earthquakeNo}", inline=True)              #編號
  embed.add_field(name="震央位置", value=f"{location}", inline=True)              #震央位置
  embed.add_field(name="發生時間", value=f"{originTime}", inline=True)            #發生時間
  embed.add_field(name=f"{magnitdueType}", value=f"{magnitudeValue}", inline=True) #規模
  embed.add_field(name="深度", value=f"{value}{unit}", inline=True)               #發生時間
  embed.set_footer(text="地震報告提供", icon_url='https://media.discordapp.net/attachments/345147297539162115/732527875839885312/ROC_CWB.png')
  await channel.send(embed=embed)

async def NEWMOHW(channel, url):
  rss = feedparser.parse(url)
  oaoa = rss['entries'][0]['title']
  owow = rss.entries[0]['summary']
  link = rss.entries[0]['link']
  text = re.sub("<.*?>", "", owow)
  nowtime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
  embed = discord.Embed(title=f'{oaoa}', color=discord.Colour.blue())
  embed.set_author(name='衛生福利部公告',
                    icon_url='https://images-ext-1.discordapp.net/external/xrfvu0X7I_vcTEmPlp0x5JqmlM9D17azlTEbYTOVFlM/https/upload.wikimedia.org/wikipedia/commons/thumb/a/a3/ROC_Ministry_of_Health_and_Welfare_Seal.svg/1200px-ROC_Ministry_of_Health_and_Welfare_Seal.svg.png?width=677&height=677')
  embed.add_field(name='新聞連結', value=f'[點擊此處]({link})', inline=False)
  embed.add_field(name='內容', value=f'{text}', inline=False)
  embed.set_footer(text=f'衛生福利部RSS服務提供• {nowtime} ',
                    icon_url='https://images-ext-1.discordapp.net/external/xrfvu0X7I_vcTEmPlp0x5JqmlM9D17azlTEbYTOVFlM/https/upload.wikimedia.org/wikipedia/commons/thumb/a/a3/ROC_Ministry_of_Health_and_Welfare_Seal.svg/1200px-ROC_Ministry_of_Health_and_Welfare_Seal.svg.png?width=677&height=677')

  await channel.send(embed=embed)