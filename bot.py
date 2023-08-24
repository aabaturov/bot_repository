import telebot
import config
from telebot import types
from menu import open_menu
from sendings import send_name_message, send_id_message, send_photo_message, send_sticker, send_test_audio, send_selfie, send_photo_from_high_school, send_hobby_text, send_sql_voice, send_GPT_voice, send_lovestory_voice, send_greetings

bot = telebot.TeleBot(config.TOKEN)
status = -1 # -1 - bot off; 0 - main menu; 1 - photo 2 - voice

@bot.message_handler(commands=['start'])
def welcome(message):
    global status
    status = 0
    
    bot.send_message(message.chat.id,
    "Добро пожаловать, {0.first_name}!\nЯ - {1.first_name}, тестовый бот для знакомства с Александром Абатуровым.\nДля взаимодействия со мной можешь воспользоваться меню или использовать текстовые команды. \nЯ могу отправить тебе фотографию, рассказать о хобби или прислать голосовое сообщение.\n\nПожалуйста, помни, что я могу принимать только те текстовые команды, которые указаны в меню на момент отправки.\nТакже всегда готов принять сообщение с текстом 'Repository', тогда пришлю ссылку на свои исходники или со словом 'API', тогда переключусь в интерактивный режим.".format(
    message.from_user, bot.get_me()), parse_mode='html')
    open_menu(message)
    
@bot.message_handler(commands=['stop'])
def stop(message):
    global status
    #bot.send_message(message.chat.id, 'Бот остановлен', reply_markup=telebot.types.ReplyKeyboardRemove())
    status = -1
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item_start = types.KeyboardButton('/start')
    markup.add(item_start)
    bot.send_message(message.chat.id, "Бот остановлен", reply_markup = markup)  

@bot.message_handler(content_types=['audio', 'document', 'animation', 'game', 'photo', 'sticker', 'video', 'video_note', 'voice', 'contact', 'location', 'venue', 'dice', 'invoice', 'successful_payment', 'connected_website', 'poll', 'passport_data', 'web_app_data'])
def repeat(message):
    bot.send_message(message.chat.id, 'Пожалуйста, пришлите верную текстовую команду', parse_mode='html')
    
@bot.message_handler(content_types=['text'])
def repeat(message):
    global status
    if message.text == "Photo" and status == 0:
        keyboard_photo = types.ReplyKeyboardMarkup(resize_keyboard=True)
        status = 1
        key_2_1 = types.KeyboardButton('Selfie')
        key_2_2 = types.KeyboardButton('High school')
        key_2_3 = types.KeyboardButton('Back')
        keyboard_photo.add(key_2_1, key_2_2, key_2_3)  # key_2_1 не использовалась

        bot.send_message(message.chat.id, 'Выберите фотографию для отправки', reply_markup=keyboard_photo)

    elif message.text == "Hobby" and status == 0:
        bot.send_message(message.chat.id, 'Тут придёт текст с рассказом об увлечении')
        send_hobby_text(message)
                         
    elif message.text == "Voice" and status == 0:
        keyboard_voice = types.ReplyKeyboardMarkup(resize_keyboard=True)
        status = 2
        key_3_1 = types.KeyboardButton('GPT explain')
        key_3_2 = types.KeyboardButton('SQL/NoSQL diff')
        key_3_3 = types.KeyboardButton('Lovestory')
        key_3_4 = types.KeyboardButton('Back')
        keyboard_voice.add(key_3_1, key_3_2, key_3_3, key_3_4)

        bot.send_message(message.chat.id, 'Выберите аудио для отправки', reply_markup=keyboard_voice)
    
    elif message.text == "Back" and (status == 1 or status == 2):
        status = 0
        open_menu(message)
    	
    elif message.text == 'Selfie' and status == 1:
    	bot.send_message(message.chat.id, 'Сейчас придёт селфи')
    	send_selfie(message)
    
    elif message.text == 'High school' and status == 1:
    	bot.send_message(message.chat.id, 'Сейчас придёт фотка из старшей школы')
    	send_photo_from_high_school(message)
    	
    elif message.text == 'GPT explain' and status == 2:
    	bot.send_message(message.chat.id, 'Пару секунд...')
    	send_GPT_voice(message)
    	
    elif message.text == 'SQL/NoSQL diff' and status == 2:
    	bot.send_message(message.chat.id, 'Пару секунд...')
    	send_sql_voice(message)
    	
    elif message.text == 'Lovestory' and status == 2:
    	bot.send_message(message.chat.id, 'Пару секунд...')
    	send_lovestory_voice(message)
    	
    elif message.text == 'Repository':
        bot.send_message(message.chat.id, 'Вот ссылка на репозиторий со мной: ')
        bot.send_message(message.chat.id, 'https://github.com/aabaturov/bot_repository')
        
    elif message.text == 'API':
        bot.send_message(message.chat.id, 'Функция находится в разработке..')
        #activate_api_mode(message)
            	
    else:
        bot.send_message(message.chat.id, 'Пожалуйста, пришли верную команду, доступную на данном уровне меню.')

     
#RUN
print('successfully started')
bot.polling(non_stop=True)
print('successfully stopped')
