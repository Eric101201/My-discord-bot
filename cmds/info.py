from discord import Embed, VerificationLevel, VoiceRegion, Member
from discord.ext import commands

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def userinfo(self, ctx, member: Member):
        roles = [role for role in member.roles] # 計算身分組
        embed = Embed(color=0x00ff40)
        embed.set_thumbnail(url=member.avatar_url) # 用戶的頭貼
        embed.add_field(name="對方名稱",value=member,inline=True) # 顯示名稱
        embed.add_field(name="對方暱稱",value=member.display_name,inline=True) # 顯示在此群的名稱
        embed.add_field(name="創建日期",value=member.created_at.strftime("%Y.%m.%d-%H:%M:%S (UTC)"),inline=False) # 顯示創建日期
        embed.add_field(name="加入日期",value=member.joined_at.strftime("%Y.%m.%d-%H:%M:%S (UTC)"),inline=False) # 顯示加入日期
        if member.is_on_mobile() == True:
            # 如手機在線
            embed.add_field(name="對方狀態",value="Moblie Online",inline=True) # 顯示對方狀態
        else:
            # 不是手機在線
            embed.add_field(name="對方狀態",value=member.status,inline=True) # 顯示對方狀態
        embed.add_field(name="機器人",value=member.bot,inline=True) # 顯示對方狀態
        embed.add_field(name=f"身分組：{len(roles)}",value=" ".join([role.mention for role in roles]),inline=False) # 顯示身分組
        embed.set_footer(text=f"user ID:{member.id}")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def serverinfo(self, ctx):
        membercounts = {"botcount": 0, "membercount": 0}
        statuses = {"online": 0, "donotdisturb": 0, "idle": 0, "offline": 0}
        channel = {"category": len(ctx.guild.categories),
                   "textchannel": len(ctx.guild.channels) - len(ctx.guild.voice_channels),
                   "voicechannel": len(ctx.guild.voice_channels)}
        safety = {"2fa level": ctx.guild.mfa_level, "verification level": ctx.guild.verification_level}
        region = ctx.guild.region

        '''計算機器人與使用者數量'''
        for mem in ctx.guild.members:
            if mem.bot:
                membercounts['botcount'] += 1
            else:
                membercounts['membercount'] += 1

        '''計算各使用者與機器人之狀態'''
        for mem in ctx.guild.members:
            if str(mem.status) == "online":
                statuses['online'] += 1
            elif str(mem.status) == "idle":
                statuses['idle'] += 1
            elif str(mem.status) == "dnd":
                statuses['donotdisturb'] += 1
            elif str(mem.status) == "offline":
                statuses['offline'] += 1

        '''驗證層級轉換'''
        if safety['verification level'] == VerificationLevel.none:
            safety['verification level'] = "無設定"
        elif safety['verification level'] == VerificationLevel.low:
            safety['verification level'] = "低驗證層級"
        elif safety['verification level'] == VerificationLevel.medium:
            safety['verification level'] = "中驗證層級"
        elif safety['verification level'] == VerificationLevel.high or safety[
            'verification level'] == VerificationLevel.table_flip:
            safety['verification level'] = "高驗證層級"
        elif safety['verification level'] == VerificationLevel.extreme or safety[
            'verification level'] == VerificationLevel.double_table_flip:
            safety['verification level'] = "最高驗證層級"

        '''是否啟用2FA'''
        if safety['2fa level'] == 1:
            safety['2fa level'] = '是'
        elif safety['2fa level'] == 0:
            safety['2fa level'] = '否'

        '''轉換地區'''
        if region == VoiceRegion.amsterdam:
            region = "荷蘭阿姆斯特丹"
        elif region == VoiceRegion.brazil:
            region = "巴西"
        elif region == VoiceRegion.dubai:
            region = "杜拜"
        elif region == VoiceRegion.eu_central:
            region = "中歐"
        elif region == VoiceRegion.eu_west:
            region = "西歐"
        elif region == VoiceRegion.europe:
            region = "歐洲"
        elif region == VoiceRegion.frankfurt:
            region = "德國法蘭克福"
        elif region == VoiceRegion.hongkong:
            region = "香港"
        elif region == VoiceRegion.india:
            region = "印度"
        elif region == VoiceRegion.japan:
            region = "日本"
        elif region == VoiceRegion.london:
            region = "英國倫敦"
        elif region == VoiceRegion.russia:
            region = "俄羅斯"
        elif region == VoiceRegion.singapore:
            region = "新加坡"
        elif region == VoiceRegion.southafrica:
            region = "南非"
        elif region == VoiceRegion.sydney:
            region = "澳洲雪梨"
        elif region == VoiceRegion.us_central:
            region = "美國中部"
        elif region == VoiceRegion.us_east:
            region = "美國東部"
        elif region == VoiceRegion.us_south:
            region = "美國南部"
        elif region == VoiceRegion.us_west:
            region = "美國西部"

        '''輸出嵌入式訊息'''
        embed1 = Embed(title=f"關於伺服器「{ctx.guild.name}」", description=f"關於伺服器{ctx.guild.name}的資訊", color=0x00ff40)
        embed1.add_field(name="伺服器ID", value=f"{ctx.guild.id}", inline=False)
        embed1.add_field(name=f"成員［{ctx.guild.member_count}］：",
                         value=f"使用者人數：{membercounts['membercount']}\n機器人個數：{membercounts['botcount']}\n上線人數：{statuses['online']}\n閒置狀態人數：{statuses['idle']}\n勿擾狀態人數：{statuses['donotdisturb']}\n離線人數：{statuses['offline']}",
                         inline=True)
        embed1.add_field(name=f"頻道［{len(ctx.guild.channels)}］：",
                         value=f"頻道類別數量：{channel['category']}\n文字頻道數量：{channel['textchannel']}\n語音頻道數量：{channel['voicechannel']}",
                         inline=True)
        embed1.add_field(name="安全層級", value=f"驗證等級：{safety['verification level']}\n兩步驟驗證是否啟用：{safety['2fa level']}",
                         inline=True)
        embed1.add_field(name="伺服器地區", value=f"{region}", inline=True)
        embed1.add_field(name="伺服器創建時間", value=f"{ctx.guild.created_at.strftime('%Y/%m/%d %p %I:%M:%S %Z')}")
        embed1.add_field(name="服主", value=f"{ctx.guild.owner.mention}")
        embed1.set_thumbnail(url=ctx.guild.icon_url)
        embed1.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed1)

def setup(bot):
    bot.add_cog(info(bot))