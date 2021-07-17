import discord
import aiohttp

from discord.ext import commands
from pyfiglet import Figlet

prefix = 'w+'

class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def editmessage(self, ctx, chann: int, id: int, *, newmsg: str):
        try:
            cha = self.bot.get_channel(chann)
            msg = await cha.fetch_message(id)
        except discord.errors.NotFound:
            await ctx.send(f'查無此`{id}`')
            return
        if msg.author != ctx.guild.me:
            await ctx.send("那個訊息TMD不是我說的")
            return
        owo = await msg.edit(content=newmsg)
        await ctx.send(f'修改完畢[點我傳送AWA]({owo.jump_url})')

    @commands.command()
    async def test(self, ctx, arg):

        f = Figlet(font='slant')
        ttt = f.renderText(arg)
        await ctx.send(f'```{ttt}```')
        print(ttt)

def setup(bot):
    bot.add_cog(test(bot))