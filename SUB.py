# GitHub: TgSweeSoft

import asyncio
import datetime
import os
import random
from time import gmtime, sleep, strftime

import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from pyrogram import Client, enums, filters, idle, sync
from simpledemotivators import Demotivator

with open('SweeUserBot/session.txt', 'r') as session_file:
    session = session_file.read()

os.system("clear")
app = Client(str(int(session)), api_id=1016382, api_hash='c27834e5683d50a9bacf835a95ec4763')


app.start()

app.stop()
os.system("clear")
print('''•·•·•·•·•·•·•·•·•·•·•·•·•·•·•··•·•·•·•·•·•·•·•·•·•·•·•·•·•·•
           SweeUserBot-V2.0 Beta


Скрипт SweeUserBot запущен теперь можешь зайти в
telegram и в любом чате(группе) написать .help
и ты получишь список всех анимаций!


ЕСЛИ ЗАКРОЕШЬ Pydroid СКРИПТ РОБОТАТЬ НЕ БУДЕТ
(потому что он не черный)!''')


@app.on_message(filters.command("help", prefixes=".") & filters.me)
def help(app, message):
    app.send_message(message.chat.id, f'''
📙<b> Functions:</b> \n<b>
1).plus
2).snow
3).hui
4).rep
5).binary_code
6).eroglifs
7).random
8).gule
9).spam
10).like
11).dislike
12).heart
13).mk
14).pidor
15).zaeb
16).fancy_text
17).orel_and_reshka
18).time
19).date
20).time_date
21).timer
22).phone_number_info
23).elapsed_time_period
24).calculator
25).pasxalka
26).real_time_in_bio
27).export_sesion_string
28).demontivator
29).from_users
30).full_info_message
31).send_reaction_for_all_messages_from_user
32).get_chat_members


🎫 Author: @ROmAanChiG


''', disable_web_page_preview=True)


@app.on_message(filters.command("plus", prefixes=".") & filters.me)
def plus(app, message):
    for i in range(1):
        message.edit(f'''
➕
''')
    sleep(3)
    message.edit(f'''
хуета..
''')
    sleep(2)
    message.edit(f'''
🔲
''')
    sleep(0.1)
    message.edit(f'''
🔲🔲
''')
    sleep(0.1)
    message.edit(f'''
🔲🔲🔲⬜️⬜️
''')
    sleep(0.1)
    message.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
''')
    sleep(0.1)
    message.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲
''')
    sleep(0.1)
    message.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲
''')
    sleep(0.1)
    message.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
''')
    sleep(0.1)
    message.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲
''')
    sleep(0.1)
    message.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️
''')
    sleep(0.1)
    message.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲
''')
    sleep(0.1)
    message.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
''')
    sleep(0.1)
    message.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️
''')
    sleep(0.1)
    message.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️
''')
    sleep(0.1)
    message.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️⬜️⬜️
''')
    sleep(0.1)
    message.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️
''')
    sleep(0.1)
    message.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️
''')
    sleep(0.1)
    message.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️
''')
    sleep(0.1)
    message.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
🔲
''')
    sleep(0.1)
    message.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️
''')
    sleep(0.1)
    message.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲
''')
    sleep(0.1)
    message.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
''')



@app.on_message(filters.command("snow", prefixes=".") & filters.me)
def snow(app, message):
    for _ in range(3):
        message.edit(f'''
 ❄
                  ❄
      ❄
            ❄
     ❄                     ❄
          ❄
''')
        sleep(0.1)
        message.edit(f'''
  ❄
               ❄
    ❄
              ❄
       ❄                  ❄
             ❄
''')
        sleep(0.1)
        message.edit(f'''
       ❄
                  ❄
      ❄
              ❄
      ❄                     ❄
                    ❄
''')
        sleep(0.1)
        message.edit(f'''
  ❄
                   ❄
      ❄
             ❄
       ❄                    ❄
          ❄
''')
        sleep(0.1)
        message.edit(f'''
     ❄
              ❄
    ❄
             ❄
         ❄            ❄
      ❄
''')
        sleep(0.1)




@app.on_message(filters.command("hui", prefixes=".") & filters.me)
def hui(app, message):
    for i in range(1):
        message.edit(f'''
    🍆🍆   🍆🍆
''')
    sleep(0.1)
    message.edit(f'''
 🍆🍆🍆  🍆🍆🍆
    🍆🍆   🍆🍆
''')
    sleep(0.1)
    message.edit(f'''
   🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆   🍆🍆
''')
    sleep(0.1)
    message.edit(f'''
      🍆🍆🍆
   🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆   🍆🍆
''')
    sleep(0.1)
    message.edit(f'''
     🍆🍆🍆
      🍆🍆🍆
   🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
  🍆🍆     🍆🍆
''')
    sleep(0.1)
    message.edit(f'''
      🍆🍆🍆
       🍆🍆🍆
        🍆🍆🍆
    🍆🍆🍆🍆🍆🍆
   🍆🍆🍆  🍆🍆🍆
    🍆🍆     🍆🍆
''')
    sleep(0.1)
    message.edit(f'''
     🍆🍆🍆
      🍆🍆🍆
       🍆🍆🍆
        🍆🍆🍆
     🍆🍆🍆🍆🍆🍆
    🍆🍆🍆  🍆🍆🍆
     🍆🍆     🍆🍆
''')
    sleep(0.1)
    message.edit(f'''
 🍆🍆🍆
  🍆🍆🍆
   🍆🍆🍆
    🍆🍆🍆
     🍆🍆🍆
  🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
  🍆🍆     🍆🍆
''')
    sleep(0.1)
    message.edit(f'''
   🍆🍆🍆
    🍆🍆🍆
     🍆🍆🍆
      🍆🍆🍆
       🍆🍆🍆
        🍆🍆🍆
   🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆   🍆🍆
''')
    sleep(0.1)
    message.edit(f'''
🍆🍆🍆
 🍆🍆🍆
  🍆🍆🍆
   🍆🍆🍆
    🍆🍆🍆
     🍆🍆🍆
      🍆🍆🍆
       🍆🍆🍆
    🍆🍆🍆🍆🍆🍆
   🍆🍆🍆  🍆🍆🍆
    🍆🍆     🍆🍆
''')
    sleep(0.1)
    message.edit(f'''
🍆🍆
🍆🍆🍆
  🍆🍆🍆
    🍆🍆🍆
     🍆🍆🍆
      🍆🍆🍆
       🍆🍆🍆
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
           🍆🍆🍆
        🍆🍆🍆🍆🍆🍆
       🍆🍆🍆  🍆🍆🍆
        🍆🍆     🍆🍆
''')





@app.on_message(filters.command("rep", prefixes=".") & filters.me)
def rep(app, message):
    for i in range(1):
        message.edit(f'''
Ты..''')
    sleep(1)
    message.edit(f'''
Говно''')
    sleep(0.001)
    message.edit(f'''
залупа''')
    sleep(0.001)
    message.edit(f'''
пенис''')
    sleep(0.001)
    message.edit(f'''
хер''')
    sleep(0.001)
    message.edit(f'''
давалка''')
    sleep(0.001)
    message.edit(f'''
хуй''')
    sleep(0.001)
    message.edit(f'''
Головка''')
    sleep(0.001)
    message.edit(f'''
шлюха''')
    sleep(0.001)
    message.edit(f'''
жопа''')
    sleep(0.001)
    message.edit(f'''
член''')
    sleep(0.001)
    message.edit(f'''
еблан''')
    sleep(0.001)
    message.edit(f'''
петух''')
    sleep(0.001)
    message.edit(f'''
мудила''')
    sleep(0.001)
    message.edit(f'''
Рукоблуд''')
    sleep(0.001)
    message.edit(f'''
ссанина''')
    sleep(0.001)
    message.edit(f'''
очко''')
    sleep(0.001)
    message.edit(f'''
блядун''')
    sleep(0.001)
    message.edit(f'''
вагина''')
    sleep(0.001)
    message.edit(f'''
Сука''')
    sleep(0.001)
    message.edit(f'''
ебланище''')
    sleep(0.001)
    message.edit(f'''
влагалище''')
    sleep(0.001)
    message.edit(f'''
пердун''')
    sleep(0.001)
    message.edit(f'''
дрочила(я тож)''')
    sleep(0.001)
    message.edit(f'''
Пидор''')
    sleep(0.001)
    message.edit(f'''
пизда''')
    sleep(0.001)
    message.edit(f'''
туз''')
    sleep(0.001)
    message.edit(f'''
мудила''')
    sleep(0.001)
    message.edit(f'''
гомик''')
    sleep(0.001)
    message.edit(f'''
малафья''')
    sleep(0.001)
    message.edit(f'''
пилотка''')
    sleep(0.001)
    message.edit(f'''
манда''')
    sleep(0.001)
    message.edit(f'''
Анус''')
    sleep(0.001)
    message.edit(f'''
вагина''')
    sleep(0.001)
    message.edit(f'''
путана''')
    sleep(0.001)
    message.edit(f'''
педрила''')
    sleep(0.001)
    message.edit(f'''
шалава''')
    sleep(0.001)
    message.edit(f'''
хуила''')
    sleep(0.001)
    message.edit(f'''
мошонка''')
    sleep(0.001)
    message.edit(f'''
елда.''')


@app.on_message(filters.command("binary_code", prefixes=".") & filters.me)
def binary_code(app, message):
    for i in range(9):
        message.edit(f'''
0 1 0 1 0 0 1 0 1 1 0 1 1 0 0
1 0 1 0 1 0 1 0 1 0 1 0 0 1 1
0 1 1 0 0 0 1 1 0 1 0 1 0 0 1
1 1 0 1 0 1 1 1 0 1 0 0 0 1 0
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
''')
    sleep(0.001)
    message.edit(f'''
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
1 0 1 0 1 0 1 0 1 0 1 0 0 1 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
0 1 1 0 0 0 1 1 0 1 0 1 0 0 1
1 1 0 1 0 1 1 1 0 1 0 0 0 1 0
''')
    sleep(0.001)
    message.edit(f'''
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
1 1 0 1 0 1 1 1 0 1 0 0 0 1 0
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
0 1 0 1 0 0 1 0 1 1 0 1 1 0 0
''')
    sleep(0.001)
    message.edit(f'''
0 0 1 0 1 0 1 1 0 0 1 1 0 1 1
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
1 0 1 0 1 0 0 1 1 0 0 0 1 0 1
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
0 1 1 1 1 0 1 1 1 1 0 1 0 1 0
''')
    sleep(0.001)
    message.edit(f'''
1 0 0 1 1 0 1 0 0 1 0 1 1 0 1
0 1 0 1 0 0 1 1 1 1 0 1 1 0 0
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
0 1 1 1 1 0 1 1 1 1 0 1 0 1 0
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
''')
    sleep(0.001)
    message.edit(f'''
0 1 1 0 0 0 1 1 0 1 0 1 0 0 1
1 0 1 0 1 0 0 1 1 0 0 0 1 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
1 0 0 1 1 0 1 0 0 1 0 1 1 0 1
''')
    sleep(0.001)
    message.edit(f'''
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
0 1 1 0 0 0 1 1 0 1 0 1 0 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
''')
    sleep(0.001)
    message.edit(f'''
1 1 0 1 0 1 1 1 0 1 0 0 0 1 0
0 0 1 0 1 0 1 1 0 0 1 1 0 1 1
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
1 0 1 0 1 0 0 1 1 0 0 0 1 0 1
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
''')
    sleep(0.001)
    message.edit(f'''
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
1 0 0 1 1 0 1 0 0 1 0 1 1 0 1
0 1 0 1 0 0 1 1 1 1 0 1 1 0 0
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
0 1 1 1 1 0 1 1 1 1 0 1 0 1 0
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
''')
    sleep(0.001)
    message.edit(f'''
0 1 1 0 1 0 0 1 1 0 1 1 0 1 0
1 1 0 1 0 1 1 1 0 1 0 0 0 1 0
0 0 1 0 1 0 1 1 0 0 1 1 0 1 1
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
1 0 1 0 1 0 0 1 1 0 0 0 1 0 1
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
''')
    sleep(0.001)
    message.edit(f'''
1 0 0 1 0 1 1 0 1 0 1 0 1 1 0
0 0 1 0 1 0 1 1 0 0 1 1 0 1 1
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
1 0 1 0 1 0 0 1 1 0 0 0 1 0 1
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
''')
    sleep(0.001)
    message.edit(f'''
1 0 1 0 1 0 0 1 1 0 0 0 1 0 1
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
1 0 1 0 1 0 1 0 1 0 1 0 0 1 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
0 1 1 0 0 0 1 1 0 1 0 1 0 0 1
''')
    sleep(0.001)
    message.edit(f'''
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
1 1 0 1 0 1 1 1 0 1 0 0 0 1 0
0 0 1 0 1 0 1 1 0 0 1 1 0 1 1
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
1 0 1 0 1 0 0 1 1 0 0 0 1 0 1
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
''')


@app.on_message(filters.command("eroglifs", prefixes=".") & filters.me)
def eroglifs(app, message):
    for i in range(4):
        message.edit(f'''
내가엿푸틴에서항문이빌
어먹을도대체나는해치지
않을것이그의빌어먹나문
나를메시서보낸도더런난
당신과그녀가그렇게니라
''')
    sleep(0.001)
    message.edit(f'''
난기다리고있을때기대에
대한지불을납품에어떤채
팅또는토요일에그것은로
봇을켜는현재에썼고그런
다음필요가없당신이일주
''')
    sleep(0.001)
    message.edit(f'''
그런데왜내가나에게필요
한모든일을한기회가있다
는것을내가모든일을했다
고당신의가족과아이들에
게말해야합니까일에그에
''')
    sleep(0.001)
    message.edit(f'''
아니면너무오래전에이메
일주소로편지를쓸수있지
기회를가지고있지않았다
우리가만나고토론할수있
것입니다그후년되지않습
''')
    sleep(0.001)
    message.edit(f'''
것입니다그후년되지않습
고당신의가족과아이들에
는것을내가모든일을했다
내가엿푸틴에서항문이빌
어먹을도대체나는해치지
''')


@app.on_message(filters.command("random", prefixes=".") & filters.me)
def random(app, message):
    random1 = message.text.split(" ", maxsplit=2)

    del random1[0]

    random2 = random1[0]
    random3 = random1[1]

    random4 = random.randint(int(random2), int(random3))

    message.edit(f"<b> Рандом показал число: {random4}</b>")


@app.on_message(filters.command("gule", prefixes=".") & filters.me)
def gule(app, message):
    app.send_message(message.chat.id, f'<b>1000-7=?</b>')
    sleep(4)
    i = 1000
    while i > 0:
        try:
            app.send_message(message.chat.id, f'{i} - 7 = {i-7}')
        except:
            sleep(3)

    i -= 7
    sleep(0)


@app.on_message(filters.command("spam", prefixes=".") & filters.me)
def spam(app, message):
    spam1 = message.text.split("\n", maxsplit=3)
    del spam1[0]
    print(spam1)
    spam2 = spam1[0]
    spam4 = spam1[1]
    for i in range(int(spam4)):
        app.send_message(message.chat.id, f"{spam2}")





@app.on_message(filters.command("like", prefixes=".") & filters.me)
def like(app, message):
    for i in range(1):
        message.edit(f'''
🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦️''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦️''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦🟦''')
    sleep(0.001)
    message.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦🟦🟦''')
    sleep(5)


@app.on_message(filters.command("dislike", prefixes=".") & filters.me)
def dislike(app, message):
    for i in range(1):
        message.edit(f'''
🟥''')  #
    sleep(0.001)
    message.edit(f'''
🟥🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥️''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥''')
    sleep(0.001)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥''')
    sleep(1)
    message.edit(f'''
🈲🈲🈲🈲🈲🈲🈲🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲⬜️⬜️⬜️⬜️🈲⬜️🈲
🈲🈲🈲🈲⬜️🈲🈲🈲
🈲🈲🈲🈲🈲🈲🈲🈲''')
    sleep(1)
    message.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥
''')
    sleep(1)
    message.edit(f'''
🈲🈲🈲🈲🈲🈲🈲🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲⬜️⬜️⬜️⬜️🈲⬜️🈲
🈲🈲🈲🈲⬜️🈲🈲🈲
🈲🈲🈲🈲🈲🈲🈲🈲''')
    sleep(4)


@app.on_message(filters.command("heart", prefixes=".") & filters.me)
def heart(app, message):
    for i in range(1):
        message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(0.5)
    message.edit(
        f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")
    sleep(1)



@app.on_message(filters.command("mk", prefixes=".") & filters.me)
def mk(app, message):
    orig_text = message.text.split(".mk ", maxsplit=1)[1]
    text = orig_text
    tbp = "" 
    typing_symbol = "|"

    while (tbp != orig_text):
        try:
            message.edit(tbp + typing_symbol)
            sleep(0.05)  

            tbp = tbp + text[0]
            text = text[1:]

            message.edit(tbp)
            sleep(0.05)

        except:
            sleep(3)




@app.on_message(filters.command("pidor", prefixes=".") & filters.me)
def pidor(app, message):
    perc = 0

    while (perc < 100):
        try:
            text = "Сканирование пользователя ..." + str(perc) + "%"
            message.edit(text)

            perc += random.randint(8, 13)
            sleep(0.1)

        except:
            sleep(3)

    message.edit("Пользователь успешно просканировался!")
    sleep(1)
    message.edit("Пользователь пидорас")



@app.on_message(filters.command("zaeb", prefixes=".") & filters.me)
def zaeb(app, message):
    orig_te1t = message.text.split(".zaeb ", maxsplit=1)[1]
    user_text = orig_te1t
    user_txt = user_text.replace("@", "")
    message.delete(message.chat.id)
    for i in range(50):
        try:
            app.send_message(
                message.chat.id, f"[бесим)](https://t.me/{user_txt})", disable_web_page_preview=True)
        except:
            sleep(3)

        sleep(0.5)


@app.on_message(filters.command("fancy_text", prefixes=".") & filters.me)
def fancy_text(app, message):
    message.delete(message.chat.id)
    or_ft = message.text.split(".fancy_text ", maxsplit=1)[1]
    ft = or_ft
    ft1 = ft.replace("SUB", "SweeUserBot")
    ft2 = ft1.replace("Б", "Ꮾ")
    ft3 = ft2.replace("В", "Ᏼ")
    ft4 = ft3.replace("Г", "Ꮁ")
    ft5 = ft4.replace("Д", "Ꭰ")
    ft6 = ft5.replace("Е", "Ꭼ")
    ft7 = ft6.replace("Ё", "Ё")
    ft8 = ft7.replace("Ж", "Ж")
    ft9 = ft8.replace("З", "З")
    ft10 = ft9.replace("И", "И")
    ft11 = ft10.replace("Й", "Й")
    ft12 = ft11.replace("К", "Ꮶ")
    ft13 = ft12.replace("Л", "Ꮧ")
    ft14 = ft13.replace("М", "Ꮇ")
    ft15 = ft14.replace("Н", "Ꮋ")
    ft16 = ft15.replace("О", "Ꮻ ")
    ft17 = ft16.replace("П", "П")
    ft18 = ft17.replace("Р", "Ꮲ")
    ft19 = ft18.replace("С", "Ꮯ")
    ft20 = ft19.replace("Т", "Ꭲ")
    ft21 = ft20.replace("У", "Ꭹ")
    ft22 = ft21.replace("Х", "Ꮱ")
    ft23 = ft22.replace("Ц", "Ц")
    ft24 = ft23.replace("Ч", "Ꮞ")
    ft25 = ft24.replace("Ш", "Ꮗ ")
    ft26 = ft25.replace("Щ", "Ꮗ ")
    ft27 = ft26.replace("Ь", "Ꮟ")
    ft28 = ft27.replace("Ы", "ᏏᏓ")
    ft29 = ft28.replace("Ъ", "Ъ ")
    ft30 = ft29.replace("Э", "Э")
    ft31 = ft30.replace("Ю", "ᎰᏫ")
    ft32 = ft31.replace("Я", "Я")
    ft33 = ft32.replace("a", "ᴀ")
    ft34 = ft33.replace("а", "ᴀ")
    ft35 = ft34.replace("б", "б")
    ft36 = ft35.replace("в", "ʙ")
    ft37 = ft36.replace("г", "ᴦ")
    ft38 = ft37.replace("д", "д")
    ft39 = ft38.replace("е", "ᴇ")
    ft40 = ft39.replace("ё", "ё")
    ft41 = ft40.replace("ж", "ж")
    ft42 = ft41.replace("з", "ɜ")
    ft43 = ft42.replace("и", "и")
    ft44 = ft43.replace("й", "й")
    ft45 = ft44.replace("к", "к")
    ft46 = ft45.replace("л", "ᴧ")
    ft47 = ft46.replace("м", "ʍ")
    ft48 = ft47.replace("н", "н")
    ft49 = ft48.replace("о", "ᴏ")
    ft50 = ft49.replace("п", "ᴨ")
    ft51 = ft50.replace("р", "ᴩ")
    ft52 = ft51.replace("с", "ᴄ")
    ft53 = ft52.replace("т", "ᴛ")
    ft54 = ft53.replace("у", "у")
    ft55 = ft54.replace("ш", "ɯ")
    ft56 = ft55.replace("щ", "щ")
    ft57 = ft56.replace("ь", "ь")
    ft58 = ft57.replace("ы", "ы")
    ft59 = ft58.replace("ъ", "ъ")
    ft60 = ft59.replace("э", "϶")
    ft61 = ft60.replace("ю", "ю")
    ft62 = ft61.replace("я", "я")
    ft63 = ft62.replace("ф", "ɸ")
    ft64 = ft63.replace("A", "Ꭺ")
    ft65 = ft64.replace("B", "Ᏼ")
    ft66 = ft65.replace("C", "Ꮯ")
    ft67 = ft66.replace("D", "Ꭰ")
    ft68 = ft67.replace("E", "Ꭼ")
    ft69 = ft68.replace("F", "Ꮀ")
    ft70 = ft69.replace("G", "Ꮐ")
    ft71 = ft70.replace("H", "Ꮋ")
    ft72 = ft71.replace("I", "Ꮖ")
    ft73 = ft72.replace("J", "Ꭻ")
    ft74 = ft73.replace("K", "Ꮶ")
    ft75 = ft74.replace("L", "Ꮮ")
    ft76 = ft75.replace("M", "Ꮇ")
    ft77 = ft76.replace("N", "N")
    ft78 = ft77.replace("O", "Ꮻ")
    ft79 = ft78.replace("P", "Ꮲ")
    ft80 = ft79.replace("Q", "Ꭷ")
    ft81 = ft80.replace("R", "Ꮢ")
    ft82 = ft81.replace("S", "Ꮪ")
    ft83 = ft82.replace("T", "Ꭲ")
    ft84 = ft83.replace("U", "Ꮜ")
    ft85 = ft84.replace("V", "Ꮩ")
    ft86 = ft85.replace("W", "Ꮃ")
    ft87 = ft86.replace("X", "Ꮱ")
    ft88 = ft87.replace("Y", "Ꭹ")
    ft89 = ft88.replace("Z", "Ꮓ")
    ft90 = ft89.replace("a", "ᴀ")
    ft91 = ft90.replace("b", "ʙ")
    ft92 = ft91.replace("c", "ᴄ")
    ft93 = ft92.replace("d", "d")
    ft94 = ft93.replace("e", "ᴇ")
    ft95 = ft94.replace("f", "f")
    ft96 = ft95.replace("g", "g")
    ft97 = ft96.replace("h", "h")
    ft98 = ft97.replace("i", "i")
    ft99 = ft98.replace("j", "j")
    ft100 = ft99.replace("k", "ᴋ")
    ft101 = ft100.replace("l", "l")
    ft102 = ft101.replace("m", "ʍ")
    ft103 = ft102.replace("n", "n")
    ft104 = ft103.replace("o", "ᴏ")
    ft105 = ft104.replace("p", "ᴩ")
    ft106 = ft105.replace("q", "q")
    ft107 = ft106.replace("r", "r")
    ft108 = ft107.replace("s", "s")
    ft109 = ft108.replace("t", "ᴛ")
    ft110 = ft109.replace("u", "u")
    ft111 = ft110.replace("v", "v")
    ft112 = ft111.replace("w", "w")
    ft113 = ft112.replace("x", "x")
    ft114 = ft113.replace("y", "y")
    ft115 = ft114.replace("z", "z")
    ft116 = ft115.replace("1", "𝟷")
    ft117 = ft116.replace("2", "𝟸")
    ft118 = ft117.replace("3", "𝟹")
    ft119 = ft118.replace("4", "𝟺")
    ft120 = ft119.replace("5", "𝟻")
    ft121 = ft120.replace("6", "𝟼")
    ft122 = ft121.replace("7", "𝟽")
    ft123 = ft122.replace("8", "𝟾")
    ft124 = ft123.replace("9", "𝟿")
    ft125 = ft124.replace("0", "𝟶")
    ft126 = ft125.replace("А", "Ꭺ")
    app.send_message(message.chat.id, f"{ft126}")


@app.on_message(filters.command("orel_and_reshka", prefixes=".") & filters.me)
def orel_and_reshka(app, message):
    message.delete(message.chat.id)
    app.send_message(message.chat.id, "⌛️")
    sleep(3)

    o_r = ['Монетка показала сторону с решкой', 'Монетка показала сторону с орлом', 'Монетка показала сторону с решкой', 'Монетка показала сторону с орлом',
    'Монетка застряла в воздухе', 'Монетка показала сторону с решкой', 'Монетка показала сторону с орлом', 'Монетка показала сторону с решкой', 'Монетка показала сторону с орлом']
    o_r2 = random.choice(o_r)
    app.send_message(message.chat.id, f"{o_r2}")


@app.on_message(filters.command("time", prefixes=".") & filters.me)
def time(app, message):
    while True:
        try:
            time1 = strftime("%H:%M:%S")
            message.edit(f"{time1}")

        except:

            sleep(3)

        sleep(1)


@app.on_message(filters.command("date", prefixes=".") & filters.me)
def date(app, message):
    while True:
        try:
            date1 = strftime("%Y %m %d")
            message.edit(f"{date1}")

        except:

            sleep(3)

        sleep(1)


@app.on_message(filters.command("time_date", prefixes=".") & filters.me)
def time_date(app, message):
    while True:
        try:
            timedate1 = strftime("%a, %Y/%m/%d %Y:%m:%d")
            message.edit(f"{timedate1}")

        except:

            sleep(3)

        sleep(1)


@app.on_message(filters.command("timer", prefixes=".") & filters.me)
def timer(app, message):
    times1 = message.text.split("timer ", maxsplit=1)[1]
    tm1 = times1
    for i in range(int(tm1)):
        message.edit(tm1)
    tm1 = int(tm1) - 1
    sleep(1)
    app.send_message(message.chat.id, 'Конец таймера')



@app.on_message(filters.command("phone_number_info", prefixes=".") & filters.me)
def phone_number_info(app, message):
    message.delete(message.chat.id)
    pi_text = message.text.split(".pi ", maxsplit=1)[1]
    pi_txt = pi_text
    pi_nomer = pi_txt.replace(" ", "")
    numb_tel_pi = phonenumbers.parse(f'{pi_nomer}')
    if pi_nomer == '+380687891388':
        app.send_message(message.chat.id, "Ошибка - 69")
    elif pi_nomer == '380687891388':
        app.send_message(message.chat.id, "Ошибка - 69")
    else:
        valid_pi = phonenumbers.is_valid_number(numb_tel_pi)
    if valid_pi == False:
        app.send_message(message.chat.id, 'Не известный номер')
    elif valid_pi == True:
        zone_tel = timezone.time_zones_for_number(numb_tel_pi)
        operator = carrier.name_for_number(numb_tel_pi, 'eu')
        region = geocoder.description_for_number(numb_tel_pi, 'eu')
        app.send_message(message.chat.id, f'''Часовой пояс: {' ' .join(zone_tel)}
Оператор: {operator}
Регион: {region}
{numb_tel_pi}

Telegram: http://t.me/{pi_nomer}
Whatsapp: https://transitapp.com/redirect.html?url=whatsapp://send/?phone={pi_nomer}
Viber: https://transitapp.com/redirect.html?url=viber://chat?number={pi_nomer}''')
    else:
        app.send_message(message.chat.id, 'Не известная ошибка')





@app.on_message(filters.command("elapsed_time_period", prefixes=".") & filters.me)
def elapsed_time_period(app, message):
    d1 = message.text.split(".tl ", maxsplit=1)[1]
    while True:
            try:
                d3 = datetime.datetime.today()
                d4 = datetime.datetime.strptime(d1, '%Y/%m/%d %H:%M:%S')
                d5 = d3 - d4
                d6 = f'{d5}'
                d7 = d6.replace('days', 'Дней')
                d8 = d7[:18]
                d9 = d8.replace('.', '')
                message.edit(f"{d9}")
            except:
                sleep(3)
            sleep(1)


@app.on_message(filters.command("calculator", prefixes=".") & filters.me)
def calculator(app, message):

    calculator1 = message.text.split(".kr ", maxsplit=1)[1]
    calculator2 = calculator1

    calculator3 = eval(calculator2)

    message.edit(f"{calculator2} = {calculator3}")


@app.on_message(filters.command("277353", prefixes="") & filters.me)
def pasxalka(app, message):
    message.edit("пасхалка!")
    sleep(1)
    app.send_message(message.chat.id, '''⣿⣿⣿⣿⠛⠛⠉⠄⠁⠄⠄⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡇⠄⠄⠄⠐⠄⠄⠄⠄⠄⠄⠄⠠⣿⣿⣿⣿⣿⣿
⣿⣿⡇⠄⢀⡀⠠⠃⡐⡀⠠⣶⠄⠄⢀⣿⣿⣿⣿⣿⣿
⣿⣿⣶⠄⠰⣤⣕⣿⣾⡇⠄⢛⠃⠄⢈⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡇⢀⣻⠟⣻⣿⡇⠄⠧⠄⢀⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣟⢸⣻⣭⡙⢄⢀⠄⠄⠄⠈⢹⣯⣿⣿⣿⣿⣿
⣿⣿⣿⣭⣿⣿⣿⣧⢸⠄⠄⠄⠄⠄⠈⢸⣿⣿⣿⣿⣿
⣿⣿⣿⣼⣿⣿⣿⣽⠘⡄⠄⠄⠄⠄⢀⠸⣿⣿⣿⣿⣿
⡿⣿⣳⣿⣿⣿⣿⣿⠄⠓⠦⠤⠤⠤⠼⢸⣿⣿⣿⣿⣿
⡹⣧⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⢇⣓⣾⣿⣿⣿⣿⣿
⡞⣸⣿⣿⢏⣼⣶⣶⣶⣶⣤⣶⡤⠐⣿⣿⣿⣿⣿⣿⣿
⣯⣽⣛⠅⣾⣿⣿⣿⣿⣿⡽⣿⣧⡸⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡷⠹⠛⠉⠁⠄⠄⠄⠄⠄⠄⠐⠛⠻⣿⣿⣿⣿
⣿⣿⣿⠃⠄⠄⠄⠄⠄⣠⣤⣤⣤⡄⢤⣤⣤⣤⡘⠻⣿
⣿⣿⡟⠄⠄⣀⣤⣶⣿⣿⣿⣿⣿⣿⣆⢻⣿⣿⣿⡎⠝
⣿⡏⠄⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⣿⣿⣿⣿⠐
⣿⡏⣲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢇⣿⣿⣿⡟⣼
⣿⡠⠜⣿⣿⣿⣿⣟⡛⠿⠿⠿⠿⠟⠃⠾⠿⢟⡋⢶⣿
⣿⣧⣄⠙⢿⣿⣿⣿⣿⣿⣷⣦⡀⢰⣾⣿⣿⡿⢣⣿⣿
⣿⣿⣿⠂⣷⣶⣬⣭⣭⣭⣭⣵⢰⣴⣤⣤⣶⡾⢐⣿⣿
⣿⣿⣿⣷⡘⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⢃⣼⣿⣿''')
    app.send_message(message.chat.id, '''⠄⠄⠄⠄⠄⠄⠄⠄⣀⣠⣤⣤⣤⣄⡀⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⣠⣿⣿⣿⡿⣿⡿⣗⢌⢳⡀⠄⠄⠄
⠄⠄⠄⠄⠄⣼⣿⡇⣿⠹⡸⡹⣷⡹⡎⣧⢳⠄⠄⠄
⠄⠄⠄⠄⠄⣿⣿⠱⡙⠰⣢⡱⢹⡇⡷⢸⢸⠄⠄⠄
⠄⠄⠄⠄⠄⢿⢸⡈⣉⣤⠠⣴⡄⡇⠁⠄⢸⠄⠄⠄
⠄⠄⠄⠄⠄⠸⡆⡃⡙⢍⣹⡿⢓⠄⠤⣐⡟⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠙⠾⠾⠮⢵⢸⡔⢷⣍⠉⠄⠄⠄⠄
⠄⠄⠄⠄⢀⣴⣾⣿⣷⡶⡋⢞⣎⣚⣭⣴⣶⣶⣤⡀
⠄⠄⠄⠄⢘⣛⣩⣾⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣷
⠄⠄⣀⠺⣿⣿⣿⠟⣡⣾⠿⢿⣿⣿⡎⢋⠻⣿⣿⣿
⠄⠄⣉⣠⣿⣿⡏⣼⣿⠁⠶⠄⣿⣿⡇⡼⠄⠈⠛⢿
⠄⠄⣈⠻⠿⠟⢁⠘⢿⣷⣶⣾⣿⠟⡰⠃⠄⠄⠄⠄
⠄⣴⣿⣧⢻⣿⣿⣷⣦⣬⣉⣩⣴⠞⠁⠄⠄⠄⠄⠄
⠄⠘⠿⠿⢸⣿⢸⣿⣿⣿⣿⣿⠁⠄⠄⠄⠄⠄⠄⠄
⠄⢤⡝⣧⠘⣿⢸⣿⡿⢻⣿⡿⠄⠄⠄⠄⠄⠄⠄⠄
⣜⢧⠻⣰⢇⣸⢠⣿⡅⣿⠏⣴⣧⡀⠄⠄⠄⠄⠄⠄
⠹⠢⢾⣿⣸⣿⣿⣿⢡⡏⣸⣿⣿⣷⠄⠄⠄⠄⠄⠄
⠄⣷⣦⡉⠛⠻⠿⠿⠾⠿⠿⠿⠛⢋⣁⠄⠄⠄⠄⠄
⢸⣿⣿⣿⣦⡀⠄⠄⠄⢀⣤⣶⣾⣿⣿⡆⠄⠄⠄⠄
⢸⣿⣿⣿⣿⣿⣄⠄⣾⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄
⠸⣿⣿⣿⣿⣿⣿⠄⢿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄
⠄⣿⣿⣿⣿⣿⣿⠄⠈⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄
⠄⢹⣿⣿⣿⣿⡟⠄⠄⠹⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄''')




@app.on_message(filters.command("real_time_in_bio", prefixes=".") & filters.me)
def real_time_in_bio(app, message):
    while True:
        try:
            d1 = "2021/10/12"
            d2 = d1
            d3 = datetime.datetime.today()
            d4 = datetime.datetime.strptime(d1, '%Y/%m/%d')
            d5 = d3 - d4
            d6 = f'{d5}'
            d7 = d6.replace('days', 'Дней')
            d8 = d7[:18]
            d9 = d8.replace('.', '')
            app.update_profile(bio=d9)
        except:
            sleep(3)
        sleep(1)



@app.on_message(filters.command("export_sesion_string", prefixes=".") & filters.me)
def export_sesion_string(app, message):
    export_sesion_string0 = app.export_session_string()
    app.send_message(message.chat.id, f"{export_sesion_string0}")


@app.on_message(filters.command("demontivator", prefixes=".") & filters.me)
def demontivator(app, message):
    message.edit("Демонтивация..")
    dem1 = message.text.split("\n")
    dem2 = dem1[1]
    dem3 = dem1[2]
    ph_id = message.reply_to_message.photo.file_id
    dem4 = app.download_media(message=ph_id,  in_memory=False)
    print(dem4)
    dem = Demotivator(f'{dem2}', f'{dem3}')
    dem.create(f'{dem4}', font_name="0.5s New Roman.ttf")
    message.edit("Демонтивация успешна✓")
    sleep(0.6)
    app.delete_messages(message.chat.id, message.id)
    app.send_photo(message.chat.id, photo='demresult.jpg')


@app.on_message(filters.command("from_users", prefixes=".") & filters.me)
def from_users(app, message):
    try:
        print(message)
        cn1 = message.reply_to_message.from_user
        cn2 = f"{cn1}"
        cn3 = cn2.replace('"', '')
        cn4 = cn3.replace(',', '')
        cn5 = cn4.replace('{', '')
        cn6 = cn5.replace('}', '')
        cn7 = cn6.replace(' ', '')
        cn8 = cn7.replace('_:User', 'USER\n')
        cn9 = cn8.replace('_:ChatPhoto', '')
        cn10 = cn9.replace('photo:', '\nPHOTO')
        cn11 = cn10.replace(':', ': ')
        cn12 = cn11.replace('false', '❌')
        cn13 = cn12.replace('true', '✅')
        app.send_message(message.chat.id, f"{cn13}")
    except AttributeError:
        message.edit('×SUB× | [AttributeError] - Вы НЕ ответели на сообщение(команду нужно отправлять с оветом на сообщение)')
    except:
        message.edit('×SUB× | [UnknownError] - Не известная ошибка')


@app.on_message(filters.command("full_info_message", prefixes=".") & filters.me)
def full_info_message(app, message):
    full_info_message1 = f"{message}"
    app.send_message(message.chat.id, full_info_message1)


@app.on_message(filters.command("send_reaction_for_all_messages_from_user", prefixes='.') & filters.me)
def send_reaction_for_all_messages_from_user(app, message):
    try:
        srfamfu11 = message.text.split(".srfamfu ", maxsplit=1)[1]
        srfamfu10 = f"{srfamfu11}"
        while True:
            for srfamfu0 in app.get_chat_history(message.chat.id):
                srfamfu1 = srfamfu0.from_user.id
                srfamfu2 = message.reply_to_message.from_user.id
                srfamfu3 = srfamfu0.id
                srtamfu4 = datetime.datetime.today()
                srfamfu5 = srfamfu0.text
                srtamfu6 = f"{srtamfu4}"
                srtamfu7 = srtamfu6[11:]
                srtamfu8 = srtamfu7.split('.')[0]
                if srfamfu1 == srfamfu2:
                    app.send_reaction(message.chat.id, srfamfu3, f"{srfamfu10}")
                    print(f"{srtamfu8} | {srfamfu5} --> Reacted: {srfamfu10}")
                    sleep(0.1)
    except IndexError:
        message.edit('×SUB× | [IndexError] - Вы НЕ указали реакцию после комманды\n\nПример:\n `.srfamfu ❤ `️')
    except AttributeError:
        message.edit('×SUB× | [AttributeError] - Вы НЕ ответели на сообщение(команду нужно отправлять с оветом на сообщение)')
    except Exception as ext:
        message.edit(f'×SUB× | {ext}')



@app.on_message(filters.command("get_chat_members", prefixes=".") & filters.all)
def get_chat_members(app, message):
    botsi1 = "╭━─━─━─━≪𝗕𝗢𝗧𝗦≫━─━─━─━╮"
    botsi2 = '''╰━─━─━─━≪𝗕𝗢𝗧𝗦≫━─━─━─━╯'''
    admins = []
    bots = []
    bots_admins = []
    members = []
    a = ""
    l = ""
    g = ""
    o = ""
    for m in app.get_chat_members(message.chat.id):
        m_stat = f"{m.status}"
        m_usr_is_bot = f"{m.user.is_bot}"
        if m_stat == 'ChatMemberStatus.ADMINISTRATOR':
            if m_usr_is_bot == 'False':
                print("+1 amd")
                admins.append(m)
        if m_stat == 'ChatMemberStatus.ADMINISTRATOR':
            if m_usr_is_bot == 'True':
                print("+1 bot adm")
                bots_admins.append(m)
        if m_stat == 'ChatMemberStatus.BOT':
            print("+1 bot")
            bots.append(m)
        if m_stat == 'ChatMemberStatus.MEMBER':
            print("+1 member")
            members.append(m)


    for i in members:
        a += f"@{i.user.username}\n"
        memb = '''╭━─━─━─≪𝗠𝗘𝗠𝗕𝗘𝗥𝗦≫─━─━─━╮'''
        memb1 = '''
╰━─━─━─≪𝗠𝗘𝗠𝗕𝗘𝗥𝗦≫─━─━─━╯'''
    membe = f"{memb}\n\n{a}\n\n{memb1}"

    for k in admins:
        l += f"@{k.user.username}\n"
        adm = '''╭━─━≪𝗔𝗗𝗠𝗜𝗡𝗜𝗦𝗧𝗥𝗔𝗧𝗢𝗥𝗦≫━─━╮'''
        adm1 = '''╰━─━≪𝗔𝗗𝗠𝗜𝗡𝗜𝗦𝗧𝗥𝗔𝗧𝗢𝗥𝗦≫━─━╯'''

    administ = f"{adm}\n\n{l}\n\n{adm1}"

    for h in bots:
        g += f"@{h.user.username}\n"

    botiks = f"{botsi1}\n\n{g}\n\n{botsi2}"

    for p in bots_admins:
        o += f"@{p.user.username}\n"
        bot_adm = "╭━≪𝗕𝗢𝗧𝗦-𝗔𝗗𝗠𝗜𝗡𝗜𝗦𝗧𝗥𝗔𝗧𝗢𝗥𝗦≫━╮"
        bot_adm2 = "╰━≪𝗕𝗢𝗧𝗦-𝗔𝗗𝗠𝗜𝗡𝗜𝗦𝗧𝗥𝗔𝗧𝗢𝗥𝗦≫━╯"

    botadm = f"{bot_adm}\n\n{o}\n\n{bot_adm2}"

    razrez = "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    vse_memb_boti_admini = f"{membe}\n\n{razrez}\n\n{administ}\n\n{razrez}\n\n{botiks}\n\n{razrez}\n\n{botadm}"
    app.send_message(message.chat.id, vse_memb_boti_admini)


app.run()
