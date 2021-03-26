import datetime

from pytz import timezone

async def log(name, info):
    tz = timezone('Asia/Taipei')
    nowtime = datetime.datetime.now(tz).strftime("%Y/%m/%d %H:%M:%S")

    with open('logger/cmdlogger.log', encoding='utf-8', mode='a') as logfile:
        logfile.write(f'{nowtime}:INFO:{name}:{info}\n')

async def msglog(name, info):
    tz = timezone('Asia/Taipei')
    nowtime = datetime.datetime.now(tz).strftime("%Y/%m/%d %H:%M:%S")

    with open('logger/msglog.log', encoding='utf-8', mode='a') as msglogfile:
        msglogfile.write(f'{nowtime}:INFO:{name}:{info}\n')