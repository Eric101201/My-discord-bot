import discord

from datetime import datetime
from discord.ext import commands

prefix = 'w+'

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        nowtime = datetime.now().strftime("%Y/%m/%d %H:%M")

        embed = discord.Embed(title="指令列表", description="", color=ctx.author.color)
        embed.add_field(name='》一般用戶使用OwO',
                        value=f'`{prefix}help`  指令查詢 \n'
                              f'`{prefix}info`  機器人狀態 \n'
                              f'`{prefix}ping`  機器人延遲 \n',
                        inline=False)

        embed.add_field(name='》管理員以及開發者使用',
                        value=f'`{prefix}vote`  投票功能, 主題.選項1.選項2 \n'
                              f'`{prefix}clean 數字`  刪除文字 \n'
                              f'`{prefix}kick @user 原因`  踢出使用者 \n'
                              f'`{prefix}ban @user 原因`  封鎖使用者 \n'
                              f'`{prefix}unban @user 原因`  解除封鎖使用者 \n'
                              f'`{prefix}say 內容`  讓機器人說話 \n',
                        inline=False)

        embed.set_footer(text=f'使用者: {str(ctx.author)}  在 {nowtime} 請求的資料')

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))