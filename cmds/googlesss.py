import discord

from datetime import datetime
from discord.ext import commands

prefix = 'w+'

class googlesss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='google', help='Google搜尋 <搜尋內容>')
    async def google(self, ctx, owo):
        nowtime = datetime.now().strftime("%Y/%m/%d %H:%M")

        embed = discord.Embed(color=ctx.author.color)
        embed.set_author(name='Google搜尋', icon_url='https://images-ext-2.discordapp.net/external/bwrkewR8GEjSJ_quRZZacIMm86ziMP90tBZYfC4N_p8/https/media.discordapp.net/attachments/685885846771335211/685887085370146856/768px-Google__G__Logo.svg.png')

        embed.add_field(name=f'》搜尋-{owo}', value=f'[點這裡!](https://www.google.com/search?q={owo})',  inline=False)

        embed.set_footer(text=f'👾 使用者: {str(ctx.author)}  在 {nowtime} 請求的資料')

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(googlesss(bot))