
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

def setup(bot):
    bot.add_cog(say(bot))