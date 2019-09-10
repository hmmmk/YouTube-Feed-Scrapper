import datetime
import hashlib
import time

import feedparser
import telegram

import config

last_post_date = datetime.datetime.now()

bot = telegram.Bot(token=config.bot_token)

last_hash = ''

while True:
    entries = feedparser.parse(config.rss_link)['entries']
    m = hashlib.sha256()
    m.update(str(entries[0]['link']).encode('utf-8'))

    if m.digest() != last_hash:
        # Logging data
        # print(entries[0]['link'])
        print(str(entries[0]))
        print(m.digest())
        bot.send_message(
            chat_id=config.channel_id,
            text=entries[0]['title'] + '\n\n' + entries[0]['link'])

        last_hash = m.digest()

    time.sleep(300)
