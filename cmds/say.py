from pytz import timezone
from datetime import datetime
from discord.ext import commands

class say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_guild_permissions(administrator=True)
    @commands.command(name='say', help='讓機器人說話 <內容>')
    async def say(self, ctx, *, arg):
        await ctx.message.delete()
        await ctx.send(arg)

    @commands.has_guild_permissions(administrator=True)
    @commands.command(name='say2', help='讓機器人說話 <頻道ID> <內容>')
    async def say2(self,ctx,cl,say):
        owo = int(cl)
        await self.bot.get_channel(owo).send(say)
        await ctx.send(f'您已讓bot在 <#{owo}> 頻道說 "{say}"')

    @commands.has_guild_permissions(administrator=True)
    @commands.command(name='send', help='匿名專用<編號> <內容>')
    async def send(self, ctx, num: str, msg: str):
        tz = timezone('Asia/Taipei')
        nowtime = datetime.now(tz).strftime("%Y/%m/%d %H:%M")
        await ctx.send(f'匿名編號：{num}\n'
                             f'匿名時間：{nowtime}\n'
                             f'匿名內容：{msg}\n')


def setup(bot):
    bot.add_cog(say(bot))