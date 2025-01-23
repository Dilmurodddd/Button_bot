import requests
import os
import json

TOKEN = os.getenv("TOKEN")

url = f"https://api.telegram.org/bot{TOKEN}/"

def get_id():
    respond = requests.get(url + 'getUpdates').json()
    return  respond['result'][-1]['message']['chat']['id']

def send_message(text, chat_id):




    keyboard_buttons = [
       [{'text': 'Tugma1 '}], [{'text': 'Tugma2 '} 
       ,{'text': 'Tugma3 '}]   
    ]
    reply_keyboard_markup = {
       'keyboard': keyboard_buttons,
       'resize_keyboard': True,
       'one_time_keyboard': True
    }
    params = {
       'chat_id': chat_id,
       'text': text,
       'reply_markup': json.dumps(reply_keyboard_markup), 
    }
   
    r = requests.get(url, params=params)
    return r.json()

print(get_id())

chat_id = get_id()
send_message('Assalomu alaykum bu kurslarni sotish uchun tajriba bot\no\'sizga kerakli tugmani bosing va kerakli ma\'lumotlarni qo\'lga kiriting!!!',chat_id)