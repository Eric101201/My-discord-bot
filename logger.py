import datetime
import logging

from pytz import timezone

async def logger2(name1, text):
    tz = timezone('Asia/Taipei')
    nowtime = datetime.datetime.now(tz).strftime("%Y/%m/%d %H:%M:%S")

    logger2 = logging.getLogger(name=name1)
    logger2.setLevel(logging.INFO)
    handler = logging.FileHandler(filename='logger/msglog.log', encoding='utf-8', mode='a')
    handler.setFormatter(logging.Formatter(f'{nowtime}:%(levelname)s:%(name)s: %(message)s'))
    logger2.addHandler(handler)
    logger2.info(text)

async def logger3(name1, tex2t):
    tz = timezone('Asia/Taipei')
    nowtime = datetime.datetime.now(tz).strftime("%Y/%m/%d %H:%M:%S")

    logger3 = logging.getLogger(name=name1)
    logger3.setLevel(logging.INFO)
    handler = logging.FileHandler(filename='logger/logfile.log', encoding='utf-8', mode='a')
    handler.setFormatter(logging.Formatter(f'{nowtime}:%(levelname)s:%(name)s: %(message)s'))
    logger3.addHandler(handler)
    logger3.info(tex2t)