import discord
import json

from discord.ext import commands
from datetime import datetime
from cmds.event import add_experience

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

with open('users.json', 'r') as f:
    users = json.load(f)

class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='開啟',help='開啟頻道 <頻道名稱>')
    @commands.guild_only()
    @commands.bot_has_guild_permissions(manage_channels=True)
    async def 開啟(self, ctx, *, name):
        user = ctx.author
        overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False),
        ctx.guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True),
        user: discord.PermissionOverwrite(read_messages=True, send_messages=True),
        }
        channel = await ctx.guild.create_text_channel(name=str(ctx.author) + f'-{name}', overwrites=overwrites, category=self.bot.get_channel(798926957135527966))
        await ctx.channel.send(f"您已開啟了新的頻道 <#{channel.id}> 。")
        await channel.send(f"{ctx.author.mention} 您已開啟新的匿名頻道 請輸入匿名的內容.")
        await channel.send("***小提示:此頻道只能交給管理員關閉,輸入完畢請標註***  `@♕蹦蹦老大♕` ***並等待管理員處理***")

    @commands.command(name='關閉',help='關閉頻道 **務必在想關閉的頻道內**')
    @commands.has_guild_permissions(administrator=True)
    @commands.has_any_role('owo', 'Bot')
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    async def 關閉(self, ctx, channel: discord.TextChannel=None, *, reason=None):
        channel = channel or ctx.channel
        await channel.delete(reason=reason)

    @commands.command(name='上鎖',help='上鎖頻道 **務必在想上鎖的頻道內 <tag user>**')
    @commands.has_guild_permissions(administrator=True)
    @commands.has_any_role('owo', 'Bot')
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    async def 上鎖(self, ctx, user: discord.Member, channel: discord.TextChannel=None):
        channel = channel or ctx.channel
        if ctx.author not in channel.overwrites:
            overwrites = {
                ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False),
                user: discord.PermissionOverwrite(send_messages=False, read_messages=False)
            }
            await channel.edit(overwrites=overwrites)
            await ctx.send(f"您已將 {user.mention} 上鎖.")
        elif channel.overwrites[user].send_messages == True or channel.overwrites[user].send_messages == None:
            overwrites = channel.overwrites[user]
            overwrites.send_messages = False
            overwrites.read_messages = False
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False)
            await channel.set_permissions(user, overwrite=overwrites)
            await ctx.send(f"您已將 {user.mention} 上鎖.")
        else:
            await ctx.send(f"您已將 {user.mention} 上鎖.")

    @commands.command(name='解鎖', help='上鎖頻道 **務必在想解鎖的頻道內 <tag user>**')
    @commands.has_guild_permissions(administrator=True)
    @commands.has_any_role('owo', 'Bot')
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    async def 解鎖(self, ctx, user: discord.Member, channel: discord.TextChannel=None):
        channel = channel or ctx.channel
        if ctx.author not in channel.overwrites:
            overwrites = {
                ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False),
                user: discord.PermissionOverwrite(send_messages=True, read_messages=True)
            }
            await channel.edit(overwrites=overwrites)
            await ctx.send(f"您已將 {user.mention} 解鎖.")
        elif channel.overwrites[user].send_messages == False or channel.overwrites[user].send_messages == None:
            overwrites = channel.overwrites[user]
            overwrites.send_messages = False
            overwrites.read_messages = False
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False)
            await channel.set_permissions(user, overwrite=overwrites)
            await ctx.send(f"您已將 {user.mention} 解鎖.")
        else:
            await ctx.send(f"您已將 {user.mention} 解鎖.")

    @commands.command(name='level', help='查詢等級')
    async def level(self, ctx, member: discord.Member = None):
        if not member:
            nowtime = datetime.now().strftime("%Y/%m/%d %H:%M")
            id = ctx.message.author.id
            lvl = users[str(id)]['level']
            exp = users[str(id)]['experience']

            embed = discord.Embed(title='等級系統', color=ctx.author.color)
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.add_field(name='目前你的等級', value=f'{lvl}', inline=False)
            embed.add_field(name='目前你的經驗值', value=f'{exp}', inline=False)
            embed.set_footer(text=f'👾 使用者: {str(ctx.author)}  在 {nowtime} 請求的資料')

            await ctx.send(embed=embed)
        else:
            nowtime = datetime.now().strftime("%Y/%m/%d %H:%M")
            id = member.id
            lvl = users[str(id)]['level']
            exp = users[str(id)]['experience']

            embed = discord.Embed(title='等級系統', color=ctx.author.color)
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name=f'目前 "{member}" 的等級', value=f'{lvl}', inline=False)
            embed.add_field(name=f'目前 "{member}" 的經驗值', value=f'{exp}', inline=False)
            embed.set_footer(text=f'👾 使用者: {str(ctx.author)}  在 {nowtime} 請求的資料')

            await ctx.send(embed=embed)

    @commands.has_guild_permissions(administrator=True)
    @commands.command(name='addexp', help='新增經驗值 <數字> <tag user>')
    async def addexp(self, ctx, owo, member: discord.Member = None):
        if not member:
            nowtime = datetime.now().strftime("%Y/%m/%d %H:%M")

            await add_experience(users, ctx.author, owo)

            with open('users.json', 'w') as f:
                json.dump(users, f)
            embed = discord.Embed(title='增加經驗值', description=f'給予 {(ctx.author)} 使用者 {owo} 經驗值', color=discord.Color.orange())
            embed.set_footer(text=f'👾 使用者: {str(ctx.author)}  在 {nowtime} 請求的資料')
            await ctx.send(embed=embed)
        else:
            nowtime = datetime.now().strftime("%Y/%m/%d %H:%M")

            await add_experience(users, member, str(owo))

            with open('users.json', 'w') as f:
                json.dump(users, f)

            embed = discord.Embed(title='增加經驗值', description=f'給予 {member} 使用者 {owo} 經驗值', color=discord.Color.orange())
            embed.set_footer(text=f'👾 使用者: {str(ctx.author)}  在 {nowtime} 請求的資料')
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Main(bot))