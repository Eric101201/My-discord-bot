
from datetime import datetime
from discord import Embed
from discord.ext.commands import Cog
from discord.ext import commands

class Log(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.log_channel = self.bot.get_channel(801804861779083275)

    @Cog.listener()
    async def on_user_update(self, before, after):
        if before.name != after.name:
            embed = Embed(title="使用者名稱更改",
                          colour=after.colour,
                          timestamp=datetime.utcnow())

            embed.add_field(name="更改使用者", value=f"<@{after.id}>.")

            fields = [("更改前", before.name, True),
                      ("更改後", after.name, True)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            await self.log_channel.send(embed=embed)

        if before.discriminator != after.discriminator:
            embed = Embed(title="Discriminator change",
                          colour=after.colour,
                          timestamp=datetime.utcnow())

            fields = [("更改前", before.discriminator, True),
                      ("更改後", after.discriminator, True)]

            embed.add_field(name="更改使用者", value=f"<@{after.id}>.")

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            await self.log_channel.send(embed=embed)

        if before.avatar_url != after.avatar_url:
            embed = Embed(title="使用者頭貼更改",
                          description="上方舊頭貼, 下方新頭貼.",
                          colour=self.log_channel.guild.get_member(after.id).colour,
                          timestamp=datetime.utcnow())

            embed.add_field(name="更改使用者", value=f"<@{after.id}>.")

            embed.set_thumbnail(url=before.avatar_url)
            embed.set_image(url=after.avatar_url)

            await self.log_channel.send(embed=embed)

    @Cog.listener()
    async def on_member_update(self, before, after):
        if before.display_name != after.display_name:
            embed = Embed(title="使用者暱稱",
                          colour=after.colour,
                          timestamp=datetime.utcnow())

            embed.add_field(name="更改使用者", value=f"更改 by <@{after.id}>.")

            fields = [("更改前", before.display_name, True),
                      ("更改後", after.display_name, True)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            await self.log_channel.send(embed=embed)

        elif before.roles != after.roles:
            embed = Embed(title="身分組更新",
                          colour=after.colour,
                          timestamp=datetime.utcnow())

            embed.add_field(name="更改使用者", value=f"更改 by <@{after.id}>.")

            fields = [("更改前", ", ".join([r.mention for r in before.roles]), False),
                      ("更改後", ", ".join([r.mention for r in after.roles]), False)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            await self.log_channel.send(embed=embed)

    @Cog.listener()
    async def on_message_edit(self, before, after):
        if not after.author.bot:
            if before.content != after.content:
                embed = Embed(title="訊息修改",
                              description=f"修改 by <@{after.author.id}>.",
                              colour=after.author.colour,
                              timestamp=datetime.utcnow())

                embed.add_field(name="更改於頻道", value=f'<#{after.channel.id}>', inline=False)

                fields = [("更改前", before.content, True),
                          ("更改後", after.content, True)]

                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)

                embed.add_field(name="訊息連結",
                                value=f'[這裡]({after.jump_url})',
                                inline=False)
                await self.log_channel.send(embed=embed)

    @Cog.listener()
    async def on_message_delete(self, message):
        if not message.author.bot:
            embed = Embed(title="訊息刪除",
                          description=f"刪除 by <@{message.author.id}>.",
                          colour=message.author.colour,
                          timestamp=datetime.utcnow())
            embed.add_field(name="訊息擁有者", value=f'<@{message.author.id}>', inline=True)
            embed.add_field(name="刪除於頻道", value=f'<#{message.channel.id}>', inline=True)

            fields = [("刪除內容", message.content, False)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            embed.add_field(name="訊息連結(失效)",
                            value=f'[這裡]({message.jump_url})',
                            inline=False)

            await self.log_channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Log(bot))