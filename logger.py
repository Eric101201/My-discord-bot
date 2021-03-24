import datetime

from pytz import timezone

async def log(name, info):
    tz = timezone('Asia/Taipei')
    nowtime = datetime.datetime.now(tz).strftime("%Y/%m/%d %H:%M:%S")

    file = open('logger/cmdlogger.log', encoding='utf-8', mode='a')
    file.write(f'{nowtime}:INFO:{name}:{info}\n')
    file.close()

async def msglog(name, info):
    tz = timezone('Asia/Taipei')
    nowtime = datetime.datetime.now(tz).strftime("%Y/%m/%d %H:%M:%S")

    file = open('logger/msglog.log', encoding='utf-8', mode='a')
    file.write(f'{nowtime}:INFO:{name}:{info}\n')
    file.close()