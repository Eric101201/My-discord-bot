import discord
import json

from discord.ext import commands

with open('reloaem.json', mode='r', encoding='UTF8') as jfile:
  jdate = json.load(jfile)

class autorole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, data):
        with open('reloaem.json', mode='r', encoding='UTF8') as jfile:
            jdate1 = json.load(jfile)
        #print("----------")
        #print(data.member)
        #print(data.emoji)
        #print("----------")
        # 反應身份組
        try:
            for i in jdate1:
                message_id = i["message_id"]
                emoji = i["emoji"]
                role = i["role"]
                if data.message_id == message_id:
                    if str(data.emoji) == emoji:
                        guild = self.bot.get_guild(data.guild_id)
                        role = guild.get_role(role)
                        await data.member.add_roles(role)
                        # await data.member.send(f"你已取得 {role} 身份組")
        except:
            pass

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, data):
        #print("----------")
        #print(data.member)
        #print(data.emoji)
        #print("----------")
        guild = self.bot.get_guild(data.guild_id)
        user = guild.get_member(data.user_id)
        with open('reloaem.json', mode='r', encoding='UTF8') as jfile:
            jdate = json.load(jfile)
        for i in jdate:
            message_id = i["message_id"]
            emoji = i["emoji"]
            role = i["role"]
            if data.message_id == message_id:
                if str(data.emoji) == emoji:
                    role = guild.get_role(role)
                    await user.remove_roles(role)
                    # await user.send(f"你已移除 {role} 身份組")

def setup(bot):
    bot.add_cog(autorole(bot))
