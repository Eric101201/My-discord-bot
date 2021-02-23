from pytz import timezone
from datetime import datetime
from discord.ext import commands

prefix = 'w+'

class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='test', help='test')
    async def test(self, ctx, num: int, msg: str):


        await num.edit(content=msg)
        #tz = timezone('Asia/Taipei')
        #nowtime = datetime.now(tz).strftime("%Y/%m/%d %H:%M")
        #await ctx.send(f'匿名編號：{num}\n'
        #                     f'匿名時間：{nowtime}\n'
        #                     f'匿名內容：{msg}\n')

def setup(bot):
    bot.add_cog(test(bot))