import random
import discord
import feedparser
import re
import json

from datetime import datetime
from discord.ext import commands

prefix = 'w+'

class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='test', help='test')
    async def test(self, ctx):
        for c in ctx.guild.channels:  # iterating through each guild channel
            await c.delete()

        #while True:
        #    category = ctx.guild

        #    ticket_nr = random.randint(0, 9999)
        #    self.channel_ticket = await category.create_text_channel(f'{ticket_nr}')
        #    await self.channel_ticket.send('@everyone')
        #    await self.channel_ticket.send('@here')
        #rss_url = 'https://www.mohw.gov.tw/rss-16-1.html'
        #rss = feedparser.parse(rss_url)
        #link = rss.entries[0]['link']

        #with open('test.json', 'r', encoding='utf8') as jfile2:
        #    jdata2 = json.load(jfile2)

        #jdata2["link"] = link

        #with open('test.json', 'w', encoding='utf8') as f2:
        #    json.dump(jdata2, f2)

        #if link not in jdata2:
            #rss_url = 'https://www.mohw.gov.tw/rss-16-1.html'
            #rss = feedparser.parse(rss_url)
            #oaoa = rss['entries'][0]['title']
            #owow = rss.entries[0]['summary']
            #link = rss.entries[0]['link']

            #text = re.sub("<.*?>", "", owow)

            #nowtime = datetime.now().strftime("%Y/%m/%d %H:%M")

            #embed = discord.Embed(title=f'{oaoa}', color=discord.Colour.blue())
            #embed.set_author(name='衛生福利部公告',
             #                icon_url='https://images-ext-1.discordapp.net/external/xrfvu0X7I_vcTEmPlp0x5JqmlM9D17azlTEbYTOVFlM/https/upload.wikimedia.org/wikipedia/commons/thumb/a/a3/ROC_Ministry_of_Health_and_Welfare_Seal.svg/1200px-ROC_Ministry_of_Health_and_Welfare_Seal.svg.png?width=677&height=677')
            #embed.add_field(name='新聞連結', value=f'[點擊此處]({link})', inline=False)
            #embed.add_field(name='內容', value=f'{text}', inline=False)
            #embed.set_footer(text=f'衛生福利部RSS服務提供• {nowtime} ',
             #                icon_url='https://images-ext-1.discordapp.net/external/xrfvu0X7I_vcTEmPlp0x5JqmlM9D17azlTEbYTOVFlM/https/upload.wikimedia.org/wikipedia/commons/thumb/a/a3/ROC_Ministry_of_Health_and_Welfare_Seal.svg/1200px-ROC_Ministry_of_Health_and_Welfare_Seal.svg.png?width=677&height=677')
            #embed.add_field(name=f'{oaoa}', value=f'{owow}')

            #await ctx.send(embed=embed)
            #with open('test.json', 'w') as f2:
            #    json.dump(link, f2)


def setup(bot):
    bot.add_cog(test(bot))