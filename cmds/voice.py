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
             if after.channel.id == 808976065354530831: #動態頻道808976065354530831
                for guild in self.bot.guilds:
                    maincategory = discord.utils.get(guild.categories, id=808976065354530832) #創建頻道類別808976065354530832
                    channel3 = await guild.create_voice_channel(name=f'{member.display_name} - 的頻道', category=maincategory)
                    await channel3.set_permissions(member, connect=True)
                    await member.move_to(channel3)
                    try:
                        ydata = yamlhook("vchannel.yaml").load()
                        ydata['VOICE'].append(channel3.id)
                        yamlhook("vchannel.yaml").Operate('VOICE', ydata['VOICE'])
                    except ValueError:
                        print("not add or return1")

                    def check(x, y, z):
                        return len(channel3.members) == 0

                    await self.bot.wait_for('voice_state_update', check=check)

                    ydata = yamlhook("vchannel.yaml").load()
                    if channel3.id in ydata['VOICE']:
                        await channel3.delete()
                        try:
                            ydata = yamlhook("vchannel.yaml").load()
                            ydata['VOICE'].remove(channel3.id)
                            yamlhook("vchannel.yaml").Operate('VOICE', ydata['VOICE'])
                        except ValueError:
                            print("not add or return1")

    @commands.group(name="voice", help="語音頻道")
    async def voice(self, ctx):
        pass

    @voice.command(name="上鎖", help="上鎖房間")
    async def lock(self, ctx):
        if ctx.channel.id == 825353840361996318:
            channel = ctx.author.voice.channel
            overwrite = discord.PermissionOverwrite(connect=False)
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
            await ctx.send(f'已上鎖`{ctx.author.voice.channel}`語音頻道')

    @voice.command(name="解鎖", help="解鎖房間")
    async def unlock(self, ctx):
        if ctx.channel.id == 825353840361996318:
            channel = ctx.author.voice.channel
            overwrite = discord.PermissionOverwrite(connect=True)
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
            await ctx.send(f'已解鎖`{ctx.author.voice.channel}`語音頻道')

    @voice.command(name="名子", help="更改房間名子")
    async def name(self, ctx, name):
        if ctx.channel.id == 825353840361996318:
            channel = ctx.author.voice.channel
            await channel.edit(name=name)
            await ctx.send(f'已更改`{ctx.author.voice.channel}`語音頻道名子')

    @voice.command(name="限制", help="禁止某人進入房間")
    async def reject(self, ctx, user: discord.Member):
        if ctx.channel.id == 825353840361996318:
            channel = ctx.author.voice.channel
            overwrite = discord.PermissionOverwrite(connect=False)
            await channel.set_permissions(user, overwrite=overwrite)
            await ctx.send(f'已禁止{user.mention}進入語音頻道')

    @voice.command(name="解除限制", help="解除某人進入房間")
    async def permit(self, ctx, user: discord.Member):
        if ctx.channel.id == 825353840361996318:
            channel = ctx.author.voice.channel
            overwrite = discord.PermissionOverwrite(connect=True)
            await channel.set_permissions(user, overwrite=overwrite)
            await ctx.send(f'已解除{user.mention}進入語音頻道')

    @voice.command(name="數量", help="變更房間最大進入人數")
    async def limit(self, ctx, limit: int = None):
        if ctx.channel.id == 825353840361996318:
            if limit <= 99:
                channel = ctx.author.voice.channel
                await channel.edit(user_limit=limit)
                await ctx.send(f'已更改`{ctx.author.voice.channel}`語音頻道最大連接人數')
            else:
                await ctx.send(f'{ctx.author.mention}最大數量為**99**')




def setup(bot):
    bot.add_cog(voice(bot))