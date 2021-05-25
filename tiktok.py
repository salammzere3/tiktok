import os,random,time,telebot,requests,pathlib
from user_agent import generate_user_agent
from telebot import *
from datetime import datetime
token = '1761966750:AAESBDOlgnh0ZuKqsYV2HDWBQf4ysRa5ffY'
sudo = 528429821
s = requests.session()
print('BOT IS RUNNING >>>>>>>>>')
RunPosts = True
bot = telebot.TeleBot(token)
markup_stop = types.InlineKeyboardMarkup()
stop = types.InlineKeyboardButton(text='Stop', callback_data='stop')
markup_stop.add(stop)
time_sleep = 3
requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={sudo}&text=𝗕𝗼𝘁 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝘀𝘁𝗮𝗿𝘁𝗲𝗱 ▶ \n\n 𝗖𝗹𝗶𝗰𝗸 /start  𝗧𝗼 𝘀𝘁𝗮𝗿𝘁 𝗯𝗼𝘁 (:')
@bot.message_handler(commands=['start'])
def start(message):
    list = open('done.txt', 'r')
    li = len(list.readlines())
    idd = message.from_user.id
    markup_inline = types.InlineKeyboardMarkup()
    start = types.InlineKeyboardButton(text='Start Check ▶', callback_data='start')
    make = types.InlineKeyboardButton(text='Make List 📜', callback_data='make')
    delete = types.InlineKeyboardButton(text='Delete List 🗑', callback_data='delete')
    file = types.InlineKeyboardButton(text='Send List 📁', callback_data='file')
    donefilee = types.InlineKeyboardButton(text='Send Done Users ✅', callback_data='done')
    deletedone = types.InlineKeyboardButton(text='Delete Done Users 🗑', callback_data='deletedone')
    sid = types.InlineKeyboardButton(text='Set Session 🆔', callback_data='sid')
    emt = types.InlineKeyboardButton(text='', callback_data='emt')
    markup_inline.row_width = 2
    markup_inline.add(start, make, file, delete, donefilee, deletedone, sid, emt)
    if idd == sudo or idd == 528429821:
        if li == 0:
            bot.send_message(message.chat.id, text='𝗧𝗜𝗞𝗧𝗢𝗞 𝗖𝗛𝗘𝗖𝗞𝗘𝗥 🤍\n\n'
                                                   f'[✅] 𝗗𝗼𝗻𝗲 𝗨𝘀𝗲𝗿𝘀 : 0\n\n'
                                                   f'Ξ 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 : @T5B55\n\n'
                                                   f'Ξ 𝗔𝗽𝗽 𝗡𝗮𝗺𝗲 :@T5B55 \n\n'
                                                   f'Ξ 𝗞𝗲𝘆 :@T5B55 \n\n',
                             reply_markup=markup_inline)
        else:
            bot.send_message(message.chat.id, text='𝗧𝗜𝗞𝗧𝗢𝗞 𝗖𝗛𝗘𝗖𝗞𝗘𝗥 🤍\n\n'
                                                   f'[✅] 𝗗𝗼𝗻𝗲 𝗨𝘀𝗲𝗿𝘀 : {li}\n\n'
                                                   f'Ξ 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 : @T5B55\n\n'
                                                   f'Ξ 𝗔𝗽𝗽 𝗡𝗮𝗺𝗲 :@T5B55 \n\n'
                                                   f'Ξ 𝗞𝗲𝘆 :@T5B55 \n\n',
                             reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    global RunPosts
    if call.data == 'make':
        sent = bot.send_message(call.message.chat.id, text='🔢 𝗔𝗠𝗢𝗨𝗡𝗧 :')
        bot.register_next_step_handler(sent, length)
    if call.data == 'start':
        check(call.message)
    if call.data == 'stop':
        RunPosts = False
    elif call.data == 'delete':
        delete(call.message)

    elif call.data == 'file':
        files(call.message)
    elif call.data == 'done':
        done(call.message)
    elif call.data == 'sid':
        sent = bot.send_message(call.message.chat.id, text='🆔 𝗦𝗲𝗻𝗱 𝗦𝗲𝘀𝘀𝗶𝗼𝗻 :')
        bot.register_next_step_handler(sent, sidinput)
    elif call.data == 'deletedone':
        deletedone(call.message)
def sidinput(message):
    sid = message.text
    url = f'https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id=s2kk&app_language=en'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": generate_user_agent(),
        "Connection": "Keep-Alive",
        "Host": "www.tiktok.com",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control": "max-age=0"}
    data = ""
    cookies = {'sessionid': sid}
    res = s.get(url, data=data, headers=headers, cookies=cookies)
    markup_inline = types.InlineKeyboardMarkup()
    markup_inlinee = types.InlineKeyboardMarkup()
    start = types.InlineKeyboardButton(text='Start Check ▶', callback_data='start')
    sidd = types.InlineKeyboardButton(text='Set Session 🆔', callback_data='sid')
    markup_inlinee.row_width = 2
    markup_inline.row_width = 2
    markup_inline.add(start)
    markup_inlinee.add(sidd)
    if 'This username isn’t available.' in res.text or '"is_valid":false' in res.text or '"is_valid":true' in res.text or '"status_msg":""' in res.text:
        sidf = open("sessionid.txt", "w")
        sidf.write(sid)
        sidf.close()
        bot.send_message(message.chat.id, text='𝗗𝗼𝗻𝗲 𝘀𝗶𝗿 𝘆𝗼𝘂 𝗰𝗮𝗻 𝘀𝘁𝗮𝗿𝘁 𝗰𝗵𝗲𝗰𝗸 [✅] ',
                         reply_markup=markup_inline)
    elif '{}' in res.text:
        bot.send_message(message.chat.id,
                         text='[🛑] 𝗬𝗼𝘂𝗿 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗗 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗯𝗮𝗻𝗻𝗲𝗱',
                         reply_markup=markup_inlinee)

    elif 'Login expired' in res.text:
        bot.send_message(message.chat.id,
                         text='[⚠] 𝗬𝗼𝘂𝗿 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗗 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗲𝘅𝗽𝗶𝗿𝗲𝗱 ',
                         reply_markup=markup_inline)


def check(message):
    listt = open('list.txt', 'r')
    liii = len(listt.readlines())
    listt.close()
    cid = message.chat.id
    mid = message.message_id
    markup_inline = types.InlineKeyboardMarkup()
    sid = types.InlineKeyboardButton(text='Set Session 🆔', callback_data='sid')
    global RunPosts
    RunPosts = True
    markup_inline.add(sid)
    d = 0
    b = 0
    er = 0
    rem = liii
    sidread = open('sessionid.txt', 'r').read()
    sessioniddd = sidread
    if os.path.exists("sessionid.txt"):
        sessionidd = open('sessionid.txt', 'r')
        lis = len(sessionidd.readlines())
        sessionidd.close()
        if lis == 0:
            bot.send_message(message.chat.id, text='[⚠] 𝗬𝗼𝘂 𝗺𝘂𝘀𝘁 𝗮𝗱𝗱 ( 𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗗 ) 𝗳𝗶𝗿𝘀𝘁')
        else:
            if os.path.exists("list.txt"):
                list = open('list.txt', 'r')
                li = len(list.readlines())
                user = open('list.txt').read().splitlines()
                list.close()
                rem = li
                if li == 0:
                    bot.send_message(message.chat.id, text='Ξ 𝗬𝗼𝘂 𝘀𝗵𝗼𝘂𝗹𝗱 𝗺𝗮𝗸𝗲 𝗹𝗶𝘀𝘁 𝗳𝗶𝗿𝘀𝘁 📜')
                else:
                    while RunPosts == True:
                        for checkusers in user:
                            nowtime = datetime.now()
                            current_time = nowtime.strftime("%H:%M:%S")
                            if rem == 0:
                                bot.send_message(message.chat.id, text='𝗜 𝗰𝗵𝗲𝗰𝗸 𝗮𝗹𝗹 𝘂𝘀𝗲𝗿𝘀 𝘀𝗶𝗿 ✅!')
                                s.cookies.clear()
                                s.close()
                                RunPosts = False
                            if not RunPosts:
                                bot.send_message(message.chat.id, text='𝗜 𝗔𝗠 𝗦𝗧𝗢𝗣 ⏸')
                                s.cookies.clear()
                                s.close()
                                break
                            url = f'https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id=' + checkusers + '&app_language=en'
                            headers = {
                                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                "User-Agent": generate_user_agent(),
                                "Connection": "Keep-Alive",
                                "Host": "www.tiktok.com",
                                "Accept-Encoding": "gzip, deflate",
                                "Cache-Control": "max-age=0"}
                            data = ""
                            cookies = {'sessionid': sessioniddd}
                            res = s.get(url, data=data, headers=headers, cookies=cookies)
                            if 'This username isn’t available.' in res.text or '"is_valid":false' in res.text or '"is_valid":true' in res.text:
                                if os.path.exists('sessionid.txt'):
                                    if '"status_msg":""' in res.text and '"is_valid":true' in res.text and RunPosts == True:
                                        with open('done.txt', 'a') as x:
                                            x.write(checkusers + '\n')
                                        time.sleep(time_sleep)
                                        rem -= 1
                                        d += 1
                                        bot.edit_message_text(chat_id=cid, text='𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 ▶\n\n'
                                                                                f'[🆔] : {sidread}\n\n'
                                                                                f'Ξ 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 𝗖𝗼𝘂𝗻𝘁 : {li}\n\n'
                                                                                f'Ξ 𝗜𝗻 𝗨𝘀𝗲𝗿 : {checkusers}\n\n'
                                                                                f'[✅] 𝗗𝗼𝗻𝗲 𝗨𝘀𝗲𝗿𝘀 : {d}\n\n'
                                                                                f'[❌] 𝗕𝗮𝗱 𝗨𝘀𝗲𝗿𝘀 :   {b}\n\n'
                                                                                f'[⚠] 𝗘𝗿𝗿𝗼𝗿 𝗨𝘀𝗲𝗿𝘀 :   {er}\n\n'
                                                              , message_id=mid,
                                                              reply_markup=markup_stop)
                                        bot.send_message(message.chat.id,
                                                         text='𝗜 𝗙𝗨𝗖𝗞 𝗡𝗘𝗪 𝗨𝗦𝗘𝗥 𝗧𝗜𝗞𝗧𝗢𝗞 [✅]\n\n'
                                                              f'Ξ 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : {checkusers}\n\n'
                                                              f'Ξ 𝗧𝗶𝗺𝗲 {current_time}')

                                    elif '"is_valid":false' in res.text or '' in res.text and RunPosts == True:
                                        time.sleep(time_sleep)
                                        b += 1
                                        rem -= 1
                                        bot.edit_message_text(chat_id=cid, text='𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 ▶\n\n'
                                                                                f'🆔 : {sidread}\n\n'
                                                                                f'Ξ 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 𝗖𝗼𝘂𝗻𝘁 : {li}\n\n'
                                                                                f'Ξ 𝗜𝗻 𝗨𝘀𝗲𝗿 : {checkusers}\n\n'
                                                                                f'[✅] 𝗗𝗼𝗻𝗲 𝗨𝘀𝗲𝗿𝘀 : {d}\n\n'
                                                                                f'[❌] 𝗕𝗮𝗱 𝗨𝘀𝗲𝗿𝘀 :   {b}\n\n'
                                                                                f'[⚠] 𝗘𝗿𝗿𝗼𝗿 𝗨𝘀𝗲𝗿𝘀 :   {er}\n\n'
                                                              , message_id=mid,
                                                              reply_markup=markup_stop)
                                    else:
                                        time.sleep(time_sleep)
                                        bot.send_message(message.chat.id, text=res.text)
                                        rem -= 1
                                        er += 1
                                        bot.edit_message_text(chat_id=cid, text='𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 ▶\n\n'
                                                                                f'🆔 : {sidread}\n\n'
                                                                                f'Ξ 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 𝗖𝗼𝘂𝗻𝘁 : {li}\n\n'
                                                                                f'Ξ 𝗜𝗻 𝗨𝘀𝗲𝗿 : {checkusers}\n\n'
                                                                                f'[✅] 𝗗𝗼𝗻𝗲 𝗨𝘀𝗲𝗿𝘀 : {d}\n\n'
                                                                                f'[❌] 𝗕𝗮𝗱 𝗨𝘀𝗲𝗿𝘀 :   {b}\n\n'
                                                                                f'[⚠] 𝗘𝗿𝗿𝗼𝗿 𝗨𝘀𝗲𝗿𝘀 :   {er}\n\n'
                                                              , message_id=mid,
                                                              reply_markup=markup_stop)

                                else:
                                    bot.send_message(message.chat.id, text='Call @salammzori')
                                    break
                            elif 'Login expired' in res.text:
                                bot.send_message(message.chat.id,
                                                 text='[⚠] 𝗬𝗼𝘂𝗿 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗗 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗲𝘅𝗽𝗶𝗿𝗲𝗱',
                                                 reply_markup=markup_inline)
                                requests.session().close()
                                s.cookies.clear()
                                s.close()
                                RunPosts = False
                                break
                            elif '{}' in res.text:
                                bot.send_message(message.chat.id,
                                                 text='[🛑] 𝗬𝗼𝘂𝗿 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗗 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗯𝗮𝗻𝗻𝗲𝗱',
                                                 reply_markup=markup_inline)
                                requests.session().close()
                                s.cookies.clear()
                                s.close()
                                RunPosts = False
                                break
                            else:
                                print(res.text)
            elif liii == 0:
                bot.send_message(message.chat.id, text='𝗬𝗢𝗨 𝗦𝗛𝗢𝗨𝗟𝗗 𝗠𝗔𝗞𝗘 𝗟𝗜𝗦𝗧 𝗙𝗜𝗥𝗦𝗧 📜')

            else:
                bot.send_message(message.chat.id, text='𝗬𝗢𝗨 𝗦𝗛𝗢𝗨𝗟𝗗 𝗠𝗔𝗞𝗘 𝗟𝗜𝗦𝗧 𝗙𝗜𝗥𝗦𝗧 📜')


def length(message):
    amount = message.text
    length = bot.send_message(message.chat.id, text='🔢 𝗟𝗘𝗡𝗚𝗧𝗛 :')
    bot.register_next_step_handler(length, make, amount)


def files(message):
    file = pathlib.Path("list.txt")
    if file.exists():
        send = open('list.txt', 'rb')
        bot.send_document(message.chat.id, send)
    else:
        bot.send_message(message.chat.id, text='𝗙𝗜𝗟𝗘 𝗡𝗢𝗧 𝗙𝗢𝗨𝗡𝗗 ❌')


def done(message):
    file = pathlib.Path("done.txt")
    if file.exists():
        list = open('done.txt', 'r')
        li = len(list.readlines())
        if li == 0:
            bot.send_message(message.chat.id, text='𝗙𝗜𝗟𝗘, 𝗜𝗦 𝗘𝗠𝗣𝗧𝗬 𝗦𝗜𝗥 📂')
        else:
            send = open('done.txt', 'rb')
            bot.send_document(message.chat.id, send)
    else:
        bot.send_message(message.chat.id, text='𝗙𝗜𝗟𝗘 𝗡𝗢𝗧 𝗙𝗢𝗨𝗡𝗗 ❌')


def make(message, amount):
    markup_inline = types.InlineKeyboardMarkup()
    startt = types.InlineKeyboardButton(text='Start Check ▶', callback_data='start')
    markup_inline.row_width = 2
    markup_inline.add(startt)
    length = message.text
    amount = int(amount)
    length = int(length)
    if os.path.exists("list.txt"):
        bot.send_message(message.chat.id, text='𝗧𝗵𝗲 𝗳𝗶𝗹𝗲 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗲𝘅𝗶𝘀𝘁 𝘆𝗼𝘂 𝗺𝘂𝘀𝘁\n'
                                               '𝗗𝗲𝗹𝗲𝘁𝗲 𝗶𝘁 𝗮𝗻𝗱 𝗺𝗮𝗸𝗲 𝗻𝗲𝘄 𝗼𝗻𝗲')
    else:
        bot.send_message(message.chat.id, text='⏳ 𝗣𝗹𝗲𝗮𝘀𝗲 𝗪𝗮𝗶𝘁 >>>>')
        chars = 'abcdefghijklmnopqrstuvwxyz1234567890_.'
        for user in range(amount):
            user = ''
            for item in range(length):
                user += random.choice(chars)
            with open('list.txt', 'a') as xx:
                xx.write(user + '\n')

        bot.send_message(message.chat.id, text='𝗜 𝗔𝗠 𝗗𝗢𝗡𝗘 𝗦𝗜𝗥 ✅', reply_markup=markup_inline)


def deletedone(message):
    if os.path.exists("done.txt"):
        sidf = open("done.txt", "w")
        sidf.write('')
        bot.send_message(message.chat.id, text='𝗙𝗜𝗟𝗘 𝗛𝗔𝗦 𝗕𝗘𝗘𝗡 𝗗𝗘𝗟𝗘𝗧𝗘𝗗 ✅')
    else:
        bot.send_message(message.chat.id, text='🛑 𝗦𝗢𝗥𝗥𝗬, 𝗕𝗨𝗧 𝗧𝗛𝗘 𝗙𝗜𝗟𝗘 𝗗𝗘𝗟𝗘𝗧𝗘𝗗 𝗔𝗟𝗥𝗘𝗔𝗗𝗬',
                         parse_mode='markdown')


def delete(message):
    markup_inline = types.InlineKeyboardMarkup()
    makee = types.InlineKeyboardButton(text='Make List 📜', callback_data='make')
    markup_inline.row_width = 2
    markup_inline.add(makee)
    if os.path.exists("list.txt"):
        os.remove("list.txt")
        bot.send_message(message.chat.id, text='𝗙𝗜𝗟𝗘 𝗛𝗔𝗦 𝗕𝗘𝗘𝗡 𝗗𝗘𝗟𝗘𝗧𝗘𝗗 ✅',
                         reply_markup=markup_inline)
    else:
        bot.send_message(message.chat.id, text='🛑 𝗦𝗢𝗥𝗥𝗬, 𝗕𝗨𝗧 𝗧𝗛𝗘 𝗙𝗜𝗟𝗘 𝗗𝗘𝗟𝗘𝗧𝗘𝗗 𝗔𝗟𝗥𝗘𝗔𝗗𝗬')


try:
	bot.polling(none_stop=True)
except:
	pass
