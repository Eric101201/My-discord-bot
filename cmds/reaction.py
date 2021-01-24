import discord
import random
import asyncio
import datetime

from discord.ext import commands
from datetime import datetime
from datahook import yamlhook

class reaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    channel_ticket = None
    ticket_creator = None

    ydata = yamlhook("channel.yaml").load()

    if (ydata == None or type(ydata['ID']) is not list):
        ydata['ID'] = []

    yamlhook("channel.yaml").Operate('ID', ydata['ID'])

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        MESSAGE_ID = 800279346799444008
        CATEGORY_ID = 800231308672499713
        BOT_ID = 593746376404500490
        LOG_CHANNEL_ID = 800042340600643644
        ROLE_ID = 701784905755000874

        guild_id = payload.guild_id
        guild = self.bot.get_guild(guild_id)
        user_id = payload.user_id
        user = self.bot.get_user(user_id)
        message_id = payload.message_id
        channel = self.bot.get_channel(payload.channel_id)

        # TICKETS
        emoji = payload.emoji.name

        if message_id == MESSAGE_ID and emoji == "📩":
            self.ticket_creator = user_id

            message = await channel.fetch_message(message_id)
            await message.remove_reaction("📩", user)

            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            support_role = guild.get_role(ROLE_ID)
            category = guild.get_channel(CATEGORY_ID)
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                member: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                support_role: discord.PermissionOverwrite(read_messages=True, send_messages=True)
            }
            ticket_nr = random.randint(0, 9999)
            self.channel_ticket = await category.create_text_channel(f'{member}的匿名-{ticket_nr}', overwrites=overwrites)

            embed = discord.Embed(title="心裡有話沒地方說嗎??",color=0x0000ff)
            embed.set_author(name="匿名機器人")
            embed.add_field(name='匿名格式:', value='```-匿名模式 (1️⃣/2️⃣)：\n''-內容： \n''> \n''> \n''>  ```', inline=False)

            embed.add_field(name='這裡可以讓你匿名說出來喔!!.', value=':white_check_mark: - 輸入完畢時請點選此貼圖來通知管理員處理\n:lock: - 關閉此匿名頻道 `管理員專用` \n:floppy_disk: - 儲存頻道聊天紀錄 `管理員專用`', inline=False)

            await self.channel_ticket.send(f"{member.mention}")

            msg = await self.channel_ticket.send(embed=embed)

            await msg.add_reaction("✅")
            await msg.add_reaction("🔒")
            await msg.add_reaction("💾")
            try:
                ydata = yamlhook("channel.yaml").load()
                ydata['ID'].append(msg.id)
                yamlhook("channel.yaml").Operate('ID', ydata['ID'])
            except ValueError:
                print("not add or return")

        ydata = yamlhook("channel.yaml").load()
        if payload.message_id in ydata['ID']:

            if emoji == "✅" and user_id != BOT_ID:
                message = await channel.fetch_message(message_id)
                await message.remove_reaction("✅", user)
                await channel.send(f"此匿名頻道 <#{payload.channel_id}> 已通知管理員,請等待處理. <@&{ROLE_ID}>")

            if 800007570483707965 in list(map(lambda x: x.id, payload.member.roles)):
                if emoji == "💾" and user_id != BOT_ID:
                    message = await channel.fetch_message(message_id)
                    await message.remove_reaction("💾", user)

                    now = datetime.now()
                    time = now.strftime(str("%d.%m.%Y") + " at " + str("%H:%M"))

                    channel_log = self.bot.get_channel(LOG_CHANNEL_ID)

                    messages = await channel.history(limit=None).flatten()

                    file = open(f"{channel}.html", "a", encoding='utf8')
                    for i in messages:
                        file.write(f'[{i.created_at}]{i.author} | {i.channel.name} | {i.content}<br> \n')
                    file.close()

                    await channel_log.send(f" <#{payload.channel_id}> 頻道存檔紀錄")
                    await channel_log.send(file=discord.File(f"{channel}.html"))

                    text = f"此匿名 <#{payload.channel_id}> 以儲存, 操作者 {user.mention} 在 {time} 儲存."
                    embed = discord.Embed(
                        title="儲存匿名!",
                        description=text,
                        color=0x0000ff)

                    await channel.send(embed=embed)

                if emoji == "🔒" and user_id != BOT_ID:
                    message = await channel.fetch_message(message_id)
                    await message.remove_reaction("🔒", user)

                    now = datetime.now()
                    time = now.strftime(str("%d.%m.%Y") + " at " + str("%H:%M"))

                    channel_log = self.bot.get_channel(LOG_CHANNEL_ID)
                    text = f"此匿名 `{channel}` 即將關閉, 操作者 {user.mention} 在 {time} 刪除."

                    embed = discord.Embed(
                        title="關閉匿名!",
                        description=text,
                        color=0x0000ff)

                    await channel_log.send(embed=embed)

                    embed = discord.Embed(
                        title="關閉匿名!",
                        description=f":tickets: 匿名已關閉,操作者: {user.mention}.",
                        color=0x0000ff)

                    await channel.send(embed=embed)

                    #ydata = yamlhook("channel.yaml").load()
                    # open blacklist
                    #try:
                    #    ydata['ID'].remove(msg.id)
                    #    # blacklist remove content
                    #    yamlhook("channel.yaml").Operate('ID', ydata['ID'])
                    #except ValueError:
                    #    print("no id")

                    await asyncio.sleep(5)
                    await channel.delete()

def setup(bot):
    bot.add_cog(reaction(bot))