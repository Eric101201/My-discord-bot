import json

from discord import Member, File
from discord.ext import commands
from io import BytesIO
from requests import get as rget
from PIL import Image, ImageDraw, ImageFont



class rank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def rank(self, ctx, member: Member=None):
        await ctx.trigger_typing()
        if member is None:
            author = ctx.author
        elif member is not None:
            author = member
        if not member:
            id = ctx.message.author.id
        else:
            id = member.id

        with open('users.json', 'r') as f:
            users = json.load(f)
        level = users[str(id)]['level']
        xp2 = users[str(id)]['experience']
        if xp2 == None or level == None:
            await ctx.send('查詢失敗 : 尚未建立等級卡 聊天後就有囉')
        if xp2 != None or level != None:
            avatar_url = rget(author.avatar_url)
            avatar_io = BytesIO(avatar_url.content)
            avatar_a = Image.open(avatar_io).resize((192, 192), Image.ANTIALIAS)
            size = avatar_a.size
            r2 = min(size[0], size[1])
            avatar = Image.new('RGB', (r2, r2),(35 ,39, 42))
            (pima, pimb) = (avatar_a.load(), avatar.load())
            for i in range(r2):
                for j in range(r2):
                    if pow(abs(i - float(r2/2) + 0.5), 2) + pow(abs(j - float(r2/2) + 0.5), 2) <= pow(float(r2/2), 2):
                        pimb[i, j] = pima[i, j]
            num = int(xp2)/int((int(level)+1)**4)

            aa = []
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
            lvll = aa.index([i for i in aa if str(i[0]) == str(author.id)][0])

            image = Image.open('level/background.png')
            drawObject = ImageDraw.Draw(image)
            drawObject.ellipse((256+600,182,256+40+600,182+40),fill=(72,75,78))
            drawObject.ellipse((256,182,256+40,182+40),fill=(72,75,78))
            drawObject.rectangle((256+(40/2),182, 256+600+(40/2), 182+40),fill=(72,75,78))
            if(num<=0):
                num = 0.01
            if(num>1):
                num=1
            w = 600*num
            drawObject.ellipse((256+w,182,256+40+w,182+40),fill=(123,175,221))
            drawObject.ellipse((256,182,256+40,182+40),fill=(123,175,221))
            drawObject.rectangle((256+(40/2),182, 256+w+(40/2), 182+40),fill=(123,175,221))
            image.paste(avatar, (45, 45))
            drawObject.multiline_text((275, 123), str(author.name), fill=(246, 246, 246), font=ImageFont.truetype('level/華康兒風體W4_1.ttc', size=55))
            drawObject.multiline_text((275, 57), 'RANK', fill=(246, 246, 246), font=ImageFont.truetype('level/華康兒風體W4_1.ttc', size=37))
            drawObject.multiline_text((360, 35), '#' + str(lvll+1), fill=(246, 246, 246), font=ImageFont.truetype('level/華康兒風體W4_1.ttc', size=65))
            drawObject.multiline_text((630, 57), 'LeveL', fill=(123, 175, 221), font=ImageFont.truetype('level/華康兒風體W4_1.ttc', size=37))
            drawObject.multiline_text((720, 35), str(level), fill=(123, 175, 221), font=ImageFont.truetype('level/華康兒風體W4_1.ttc', size=65))
            xp = drawObject.textsize(str(int(xp2)) + '/' + str((int(level)+1)**4) + 'XP', font=ImageFont.truetype('level/華康兒風體W4_1.ttc', size=45))
            drawObject.multiline_text((934-xp[1]-205, 140), str(int(xp2)) + '/' + str((int(level)+1)**4) + 'XP', fill=(246, 246, 246), font=ImageFont.truetype('level/華康兒風體W4_1.ttc', size=45))
            image.save('level/rank.png')
            await ctx.send(file=File('level/rank.png'))

def setup(bot):
    bot.add_cog(rank(bot))