import json
import discord

from discord.ext import commands


class levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='levels', help='查詢排行')
    async def levels(self, ctx):
        with open('users.json', 'r') as f:
            users = json.load(f)
        aa = []
        text = []
        data = list(users.keys())
        for i in range(len(users)):
            try:
                _id = data[i]
                level = users[data[i]]["level"]
                xp = users[data[i]]["experience"]

                aa.append((int(_id), int(level), int(xp)))
            except KeyError:
                continue
        aa.sort(key=lambda x: x[2], reverse=True)
        raa = 1
        for i in aa:
            text.append(f'`#{raa} | level: {str(i[1])} , xp: {str(i[2])}` | ID: <@{str(i[0])}>\n')
            raa+=1
            if i == aa[9]:
                break
        text[0] = "**" + text[0] + "**"
        num = aa.index([i for i in aa if str(i[0]) == str(ctx.author.id)][0])
        levels = discord.Embed(title="此伺服器的等級排行(前10名)", color=0x00ff40, description="".join(text)).set_footer(text="你的排名: {}".format(num+1), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=levels)

def setup(bot):
    bot.add_cog(levels(bot))