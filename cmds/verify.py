import discord
import random
import asyncio

from discord.ext import commands

class verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='verify')
    @commands.has_any_role('未驗證')
    async def verify(self, ctx):
        longer = int(3)
        digit = int(5)
        ch_l = []
        digit_long = digit
        digit_num = int('F' * digit, 16)
        for i in range(longer):
            ch_l.append(str(hex(random.randint(0, digit_num)).replace('0x', '')).zfill(digit_long))
        code = '-'.join(ch_l)

        unverified = discord.utils.get(ctx.guild.roles, name="未驗證")
        verify = discord.utils.get(ctx.guild.roles, name="Player")

        e = discord.Embed(title='請在30秒內輸入驗證碼.',
            description='**NOTE: 一定要驗證才能進入喔❤❤**', color=discord.Color.green())
        e.add_field(name='驗證碼如下:',
            value=f'**{code}**', inline=False)
        await ctx.send(embed=e)

        def check(m):
            return m.content == code

        try:
            await self.bot.wait_for('message', check=check, timeout=30.0)
        except asyncio.TimeoutError:
            e = discord.Embed(title='30秒時間到，請重新輸入指令取得驗證碼.',
                        description='**NOTE: 一定要驗證才能進入喔❤❤**', color=discord.Color.green())

            await ctx.send(embed=e)

        else:
            e = discord.Embed(color=discord.Color.green())
            await ctx.author.remove_roles(unverified)
            e.add_field(name='您已驗證成功!!', value='您現在可以進入伺服器聊天了.')
            await ctx.send(embed=e)
            await ctx.author.add_roles(verify)


def setup(bot):
    bot.add_cog(verify(bot))