import discord

from datahook import yamlhook
from discord.ext import commands

class voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    channel3 = None

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if after.channel != None:
             if after.channel.id == 811480245089730580: #動態頻道808976065354530831
                for guild in self.bot.guilds:
                    maincategory = discord.utils.get(guild.categories, id=808976065354530832) #創建頻道類別808976065354530832
                    channel3 = await guild.create_voice_channel(name='123', category=maincategory)
                    await channel3.set_permissions(member, connect=True)
                    await member.move_to(channel3)
                    try:
                        ydata = yamlhook("channel.yaml").load()
                        ydata['VOICE'].append(channel3.id)
                        yamlhook("channel.yaml").Operate('VOICE', ydata['VOICE'])
                    except ValueError:
                        print("not add or return1")

                    def check(x, y, z):
                        return len(channel3.members) == 0

                    await self.bot.wait_for('voice_state_update', check=check)

                    ydata = yamlhook("channel.yaml").load()
                    if channel3.id in ydata['VOICE']:
                        await channel3.delete()
                        try:
                            ydata = yamlhook("channel.yaml").load()
                            ydata['VOICE'].remove(channel3.id)
                            yamlhook("channel.yaml").Operate('VOICE', ydata['VOICE'])
                        except ValueError:
                            print("not add or return1")

def setup(bot):
    bot.add_cog(voice(bot))