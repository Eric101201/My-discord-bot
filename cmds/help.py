import discord

from pytz import timezone
from datetime import datetime
from discord.ext import commands

prefix = 'w+'

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, arg = None):
        if arg == None:
            tz = timezone('Asia/Taipei')
            nowtime = datetime.now(tz).strftime("%Y/%m/%d %H:%M")

            embed = discord.Embed(title="指令列表", description="", color=ctx.author.color)
            embed.add_field(name='》一般用戶使用OwO',
                            value=f'> `w-help`  指令查詢 \n'
                                  f'> `{prefix}help admin`  管理員指令查詢 \n'
                                  f'> `{prefix}help voice`  動態語音指令查詢 \n'
                                  f'> `{prefix}info`  機器人狀態 \n'
                                  f'> `{prefix}ping`  機器人延遲 \n'
                                  f'> `{prefix}google`  Google搜尋 <搜尋內容> \n'
                                  f'> `{prefix}dcapi`  Discord.py搜尋 <搜尋內容> \n'
                                  f'> `{prefix}rank`  查詢等級 \n'
                                  f'> `{prefix}levels`  查詢排行 \n'
                                  f'> `{prefix}listinvite`  查詢此伺服器所有邀請連結 \n'
                                  f'> `{prefix}addinvite`  建立邀請連結 <邀請有效時長s> <邀請最大使用次數>',
                            inline=False)
            embed.add_field(name="About", value=f"我的指令 `{prefix}`", inline=False)
            embed.set_footer(text=f'👾 使用者: {str(ctx.author)}  在 {nowtime} 請求的資料')

            await ctx.send(embed=embed)

        elif arg == "admin":
            tz = timezone('Asia/Taipei')
            nowtime = datetime.now(tz).strftime("%Y/%m/%d %H:%M")

            embed = discord.Embed(title="指令列表", description="》管理員以及開發者使用", color=ctx.author.color)
            embed.add_field(name='> 一般',
                            value='```'
                                  f'{prefix}say         |讓機器人說話 <內容> \n'
                                  f'{prefix}say2        |讓機器人說話 <頻道ID> <內容> \n'
                                  f'{prefix}send        |匿名專用<編號> <內容> \n'
                                  f'{prefix}gstart      |抽獎系統 <抽獎倒數時間s m h d> <數量> <抽獎內容> \n'
                                  f'{prefix}vote        |投票功能, <主題> <選項1> <選項2> \n'
                                  f'{prefix}addexp      |增加經驗值 <數字> <tag user> \n'
                                  f'{prefix}reply       |回覆訊息 <頻道ID> <訊息ID> <是否tag True/False> <回覆內容>'
                                  '```',
                            inline=False)
            embed.add_field(name='> 管理',
                            value='```'
                                  f'{prefix}clean       |刪除訊息 <刪除數量> \n'
                                  f'{prefix}kick        |踢出使用者 <tag user> <原因> \n'
                                  f'{prefix}ban         |封鎖使用者 <tag user> <原因> \n'
                                  f'{prefix}unban       |解除封鎖使用者 <tag user> <原因> \n'
                                  f'{prefix}addrole     |新增反應身分組 <訊息ID> <身分組ID> <貼圖> \n'
                                  f'{prefix}editmsg     |修改機器人發送訊息 <頻道ID> <訊息ID> <修改內容>'
                                  '```',
                            inline=False)
            embed.add_field(name='> 頻道',
                            value='```'
                                  f'{prefix}開啟         |開啟頻道 <頻道名稱> \n'
                                  f'{prefix}關閉         |關閉頻道**務必在想關閉的頻道內** \n'
                                  f'{prefix}上鎖         |上鎖頻道**務必在想上鎖的頻道內** <tag user> \n'
                                  f'{prefix}解鎖         |解鎖頻道**務必在想解鎖的頻道內** <tag user>'
                                  '```',
                            inline=False)
            embed.add_field(name='> 擁有者專用',
                            value='```'
                                  f'{prefix}load        |載入 <Cog mod> \n'
                                  f'{prefix}reload      |重新載入 <Cog mod> \n'
                                  f'{prefix}unload      |移除 <Cog mod> \n'
                                  f'{prefix}rebot       |重啟機器人 \n'
                                  f'{prefix}bye         |關閉機器人 \n'
                                  f'```',
                            inline=False)

            embed.add_field(name="About", value=f"我的指令 `{prefix}`", inline=False)
            embed.set_footer(text=f'👾 使用者: {str(ctx.author)}  在 {nowtime} 請求的資料')

            await ctx.send(embed=embed)

        elif arg == "voice":
            tz = timezone('Asia/Taipei')
            nowtime = datetime.now(tz).strftime("%Y/%m/%d %H:%M")

            embed = discord.Embed(title="指令列表", description="》動態語音頻道指令", color=ctx.author.color)
            embed.add_field(name='> 指令',
                            value='```'
                                  f'{prefix}voice 上鎖　　　　|上鎖房間 \n'
                                  f'{prefix}voice 解鎖　　　　|解鎖房間 \n'
                                  f'{prefix}voice 名子　　　　|更改房間名子 <名子> \n'
                                  f'{prefix}voice 限制　　　　|禁止某人進入房間 <tag user> \n'
                                  f'{prefix}voice 解除限制　　|解除某人進入房間 <tag user> \n'
                                  f'{prefix}voice 數量　　　　|頻道最大人數 <數字> '
                                  '```',
                            inline=False)
            embed.add_field(name="About", value=f"我的指令 `{prefix}`", inline=False)
            embed.set_footer(text=f'👾 使用者: {str(ctx.author)}  在 {nowtime} 請求的資料')

            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))