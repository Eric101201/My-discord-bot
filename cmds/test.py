import discord
from discord.ext import commands

prefix = 'w+'

class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def editmessage(self, ctx, id: int, *, newmsg: str):
        """Edits a message sent by the bot"""
        try:
            msg = await ctx.channel.fetch_message(id)
        except discord.errors.NotFound:
            await ctx.send("Couldn't find a message with an ID of `{}` in this channel".format(id))
            return
        if msg.author != ctx.guild.me:
            await ctx.send("That message was not sent by me")
            return
        await msg.edit(content=newmsg)
        await ctx.send("edit af")


def setup(bot):
    bot.add_cog(test(bot))