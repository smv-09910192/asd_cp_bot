import telebot;
import dbcontext;
import Entities.invertor;

from telebot import types

bot = telebot.TeleBot('7852025083:AAE8501zgNwlrCrL4MrTb36OzNzhgE8RLls');
dbctx = dbcontext.DbContext('https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive', '')
invertors = []
batteries = []

@bot.message_handler(content_types=['text'])


def start(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Вкажіть ваше ім'я");
        bot.register_next_step_handler(message, get_name);

def get_keyboard(entities, entType):
    keyboard = types.InlineKeyboardMarkup();
    for ent in entities:
        key = types.InlineKeyboardButton(text=ent.Name, callback_data='entType|' + ent.Id); #кнопка «Да»
        keyboard.add(key);
    return keyboard;


def get_name(message): #отримуємо ім'я
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Номер телефону');
    bot.register_next_step_handler(message, get_phone);

def get_phone(message): #отримуємо номер телефону
    global name;
    name = message.text;
    invertors = dbctx.get_all_invertors()
    keyboard = get_keyboard(invertors);
    bot.send_message(message.from_user.id, 'Виберіть інвертор з ціною', reply_markup=keyboard);
    #bot.register_next_step_handler(message, get_invertor);

def get_invertor(message): #отримуємо інвертор
    global name;
    name = message.text;
    batteries = dbctx.get_all_batteries()
    keyboard = get_keyboard(batteries);
    bot.send_message(message.from_user.id, 'Виберіть батарею з ціною', reply_markup=keyboard);
    bot.register_next_step_handler(message, get_battery);

def get_battery(message): #отримуємо батарею
    global name;
    name = message.text;

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data is  None:
         bot.send_message(call.data.message.from_user.id, 'Дані не вибрані');
    else:
        datas = call.data.split('|');
        if datas[0] == 'inv':
            
        
       


bot.polling(none_stop=True, interval=0)