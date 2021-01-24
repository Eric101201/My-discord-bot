import discord
from discord.ext import commands
import json
import os
import random
import asyncio

intents = discord.Intents.all()

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
    
prefix = 'q/'
bot = commands.Bot(command_prefix=prefix, help_command=None, intents=intents, owner_ids="593666614717841419")

async def status_task():
    while True:
        await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=F"{prefix}help"))
        await asyncio.sleep(5)
        await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="堅果真好吃OwO"))
        await asyncio.sleep(5)
        await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=f'我正在 {bot.guilds}' + "個伺服器做奴隸"))
        await asyncio.sleep(5)

@bot.event
async def on_ready():
    channel = bot.get_channel(701779007980437826)
    bot.loop.create_task(status_task())
    embed2=discord.Embed(title=">>Bot on ready<<", color=(random.choice(jdata['顏色'])))
    await channel.send(embed=embed2)
    print(">> Bot is online <<")
    print(bot.user.name)
    print(bot.user.id)
    print(f'prefix:{prefix}')
    print(str(len(bot.guilds)) + " servers")
    print('========OwO========')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
