from pyrogram import Client, filters
from pyrogram import errors
import time

app = Client('BOT', api_id=1016382, api_hash='c27834e5683d50a9bacf835a95ec4763')

print('UserBot Has STARTED')

@app.on_message(filters.command('test', prefixes='.') & filters.me)
def test(app, message):
	message.reply('✅ TEST ✅')

@app.on_message(filters.command('spam', prefixes='.') & filters.me)
def spam(app, message):
    _list = str(message.text).split('\n')		
    text = str(_list[1])
    count = int(_list[2])
    delay = float(_list[3])
    print(f'Text: {text}\nCount: {count}\nDelay: {delay}')
    for _ in range(count):
        app.send_message(message.chat.id, text)
        time.sleep(delay)
        
app.run()