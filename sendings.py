import os
import telebot
import config
import random
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

def send_name_message(message):
    bot.send_message(message.chat.id,
    "Сообщение 1.\nВаше имя - {0.first_name}!\nМоё имя(жирным) - <b>{1.first_name}</b>.".format(
    message.from_user, bot.get_me()), parse_mode='html')
    
def send_id_message(message):
    bot.send_message(message.chat.id,
    "Сообщение 2.\nВаш айди - , {0.id}!\nМой айди(жирным) - <b>{1.id}</b>.".format(
    message.from_user, bot.get_me()), parse_mode='html')    

def send_greetings(message):
    greet = open('data/greetings', 'rb')
    bot.send_message(message.chat.id, greet)

def send_photo_message(message):
    number = bot.get_user_profile_photos(message.from_user.id)
    bot.send_message(message.chat.id, 
    "Сообщение 2.\nВаше фото", parse_mode='html')
    photos_ids = []
    for photo in number.photos:
        photos_ids.append(photo[0].file_id)    
    bot.send_photo(message.chat.id, photos_ids[random.randint(0,number.total_count - 1)])
    
def send_hobby_text(message):
    text = open('data/hobby', 'rb')
    bot.send_message(message.chat.id, text)
    
def send_test_audio(message):
    audio = open(r'audio/sample.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)
    audio.close()
    
def send_GPT_voice(message):
    voice = open(r'audio/gpt.ogg', 'rb')
    bot.send_voice(message.chat.id, voice, caption = 'Тут за минуту объясняю бабушке, что такое GPT', duration = 59, protect_content = True)
    
def send_sql_voice(message):
    voice = open(r'audio/sql.ogg', 'rb')
    bot.send_voice(message.chat.id, voice, caption = 'Тут за минуту объясняю бабушке разницу SQL и noSQL', duration = 59, protect_content = True)
    
def send_lovestory_voice(message):
    voice = open(r'audio/lovestory.ogg', 'rb')
    bot.send_voice(message.chat.id, voice, caption = 'Тут история из жизни (:(', duration = 59, protect_content = True)    

def send_selfie(message):
    ph = open('data/selfie.jpg', 'rb')
    bot.send_photo(message.chat.id, ph)

def send_photo_from_high_school(message):
    ph = open('data/high_school.jpg', 'rb')
    bot.send_photo(message.chat.id, ph)

def send_sticker(message):
    rand = random.randint(1,5)
    if (rand == 1):
        sti = open('stickers/sticker1.webp', 'rb')
    if (rand == 2):
        sti = open('stickers/sticker2.webp', 'rb')
    if (rand == 3):
        sti = open('stickers/sticker3.webp', 'rb')
    if (rand == 4):
        sti = open('stickers/sticker4.webp', 'rb')
    if (rand == 5):
        sti = open('stickers/AnimatedSticker.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
 
