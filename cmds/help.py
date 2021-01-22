import discord

from datetime import datetime
from discord.ext import commands

prefix = 'w+'

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help', help='指令列表')
    async def help(self, ctx):
        nowtime = datetime.now().strftime("%Y/%m/%d %H:%M")

        embed = discord.Embed(title="指令列表", description="", color=ctx.author.color)
        embed.add_field(name='》一般用戶使用OwO',
                        value=f'`{prefix}help`  指令查詢 \n'
                              f'`{prefix}info`  機器人狀態 \n'
                              f'`{prefix}ping`  機器人延遲 \n',
                        inline=False)

        embed.add_field(name='》管理員以及開發者使用',
                        value=f'`{prefix}vote`  投票功能, <主題> <選項1> <選項2> \n'
                              f'`{prefix}clean`  刪除文字 <刪除數量> \n'
                              f'`{prefix}say`  讓機器人說話 <內容> \n'
                              f'`{prefix}say2`  讓機器人說話 <頻道ID> <內容> \n'
                              f'`{prefix}開啟`  開啟頻道 <頻道名稱> \n'
                              f'`{prefix}開閉`  關閉頻道 **務必在想關閉的頻道內** \n'
                              f'`{prefix}上鎖`  上鎖頻道 **務必在想上鎖的頻道內** \n'
                              f'`{prefix}解鎖`  解鎖頻道 **務必在想解鎖的頻道內** \n'
                              f'`{prefix}kick`  踢出使用者 <tag user> <原因> \n'
                              f'`{prefix}ban`  封鎖使用者 <tag user> <原因> \n'
                              f'`{prefix}unban`  解除封鎖使用者 <tag user> <原因> \n'
                              f'`{prefix}load`  載入 <Cog mod> \n'
                              f'`{prefix}reload`  重新載入 <Cog mod> \n'
                              f'`{prefix}unload`  移除 <Cog mod> \n'
                              f'`{prefix}unban`  解除封鎖使用者 <tag user> <原因> \n'
                              f'`{prefix}bye`  關閉機器人 \n'
                              ,
                        inline=False)
        embed.add_field(name="About", value=f"我的指令 `{prefix}` | 使用 `{prefix}help <指令名稱>` 可以取得針對此指令之說明.", inline=False)
        embed.set_footer(text=f'👾 使用者: {str(ctx.author)}  在 {nowtime} 請求的資料')

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))