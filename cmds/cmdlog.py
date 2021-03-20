from discord.ext import commands
from logger import logger3

class cmdlog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command(self, ctx):
        try:
            await logger3('discord.command', f"{ctx.guild.name} > {ctx.author} > {ctx.message.clean_content}")
        except AttributeError:
            await logger3('discord.command', f"私訊 > {ctx.author} > {ctx.message.clean_content}")

def setup(bot):
    bot.add_cog(cmdlog(bot))