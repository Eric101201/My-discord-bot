import discord
from discord.ext import commands

class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ticket(self, ctx):
        title = "心裡有話沒地方說嗎?"
        description = "這裡歡迎你來說 本群提供匿名留言."
        name = "你只需要點下方 📩 貼圖就可以開啟匿名頻道."

        embed = discord.Embed(title=title, description=description, color=0x2f2fd0)
        embed.add_field(name="如何使用?", value=name, inline=True)
        embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/x7kxTszr-e7WXPCkD11lhepLD457nLcMleTA4B1t8kM/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/636559032324325417/280943367acac65988c95de80ef5a1e2.webp?width=676&height=676")
        embed.set_author(name="匿名機器人")

        msg = await ctx.send(embed=embed)
        await msg.add_reaction("📩")
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(admin(bot))