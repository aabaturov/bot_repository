import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

def open_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item_name = types.KeyboardButton('Photo')
    item_photo = types.KeyboardButton('Hobby')
    item_sticker = types.KeyboardButton('Voice')
    item_exit = types.KeyboardButton('/stop')    
    markup.add(item_name, item_photo, item_sticker, item_exit)
    
    bot.send_message(message.chat.id, "Бот работает", reply_markup = markup)
    
