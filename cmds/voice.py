import discord

from discord.ext import commands

class voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    channel2 = None

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if after.channel != None:
            if after.channel.id == 801654702991081482:
                for guild in self.bot.guilds:
                    maincategory = discord.utils.get(guild.categories, id=701434053706121249)
                    self.channel2 = await guild.create_voice_channel(name=f'{member.display_name} - 的頻道', category=maincategory)
                    await self.channel2.set_permissions(member, connect=True, mute_members=True, manage_channels=True)
                    await member.move_to(self.channel2)

                    def check(x, y, z):
                        return len(self.channel2.members) == 0

                    await self.bot.wait_for('voice_state_update', check=check)
                    await self.channel2.delete()

def setup(bot):
    bot.add_cog(voice(bot))