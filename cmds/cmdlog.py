from discord.ext import commands
from logger import log

class cmdlog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command(self, ctx):
        try:
            await log('discord.command', f"{ctx.guild.name} > {ctx.author} > {ctx.message.clean_content}")
        except AttributeError:
            await log('discord.command', f"私訊 > {ctx.author} > {ctx.message.clean_content}")

def setup(bot):
    bot.add_cog(cmdlog(bot))