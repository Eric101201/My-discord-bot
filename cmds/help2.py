import discord
import time

from datetime import datetime
from discord.ext import commands

prefix = 'w+'

class help2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help2', help='指令幫助2')
    async def help2(self, ctx: commands.Context, groupName=None):
        nowtime = datetime.now().strftime("%Y/%m/%d %H:%M")

        helpCommand = []
        helptext = []
        groupCommand = {}
        if groupName != None:
            for command in self.bot.commands:
                # find group commands
                if command.name == groupName:
                    # dict copy
                    groupCommand = command.all_commands
                    # get group commands > key
                    helpCommand = list(groupCommand.keys())
                    for i in range(len(helpCommand)):
                        # get group commands help
                        # command help is empty
                        if groupCommand[helpCommand[i]].help == None:
                            helptext.append("owo!")
                        else:
                            helptext.append(groupCommand[helpCommand[i]].help)
                    break
        else:
            for command in self.bot.commands:
                helpCommand.append(command.name)
                # command help is empty
                if command.help == None:
                    helptext.append("owo!")
                else:
                    helptext.append(command.help)
        # embed
        helpDisplay = discord.Embed(title="指令列表", color=ctx.author.color)
        for i in range(len(helpCommand)):
            if groupName == None:
                # groupName = ""
                helpDisplay.add_field(name=f"{prefix}{helpCommand[i]}", value=helptext[i], inline=False)
            else:
                helpDisplay.add_field(name=f"{prefix}{groupName} {helpCommand[i]}", value=helptext[i], inline=False)

        helpDisplay.add_field(name="About", value=f"我的指令 `{prefix}` | 使用 `{prefix}help <指令名稱>` 可以取得針對此指令之說明.", inline=False)
        helpDisplay.set_footer(text=f"👾 {nowtime}")
        await ctx.send(embed=helpDisplay)

def setup(bot):
    bot.add_cog(help2(bot))