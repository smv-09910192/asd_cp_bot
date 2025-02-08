import telebot;
import dbcontext;
import Entities.invertor;
import Entities.order

from telebot import types
from Entities.order import Order
from Entities.battery import Battery
from Entities.invertor import Invertor

bot = telebot.TeleBot('7852025083:AAE8501zgNwlrCrL4MrTb36OzNzhgE8RLls');
dbctx = dbcontext.DbContext('https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive', 'conf\\credentials.json')
order = Order();
invertors = []
batteries = []

@bot.message_handler(content_types=['text', 'document', 'audio'])

def start(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Вкажіть ваше ім'я");
        bot.register_next_step_handler(message, get_name);

def get_keyboard(entities):
    keyboard = types.InlineKeyboardMarkup();
    for ent in entities:
        data = f"{ent.Id}";
        key = types.InlineKeyboardButton(text=ent.Name, callback_data=data); #кнопка «Да»
        keyboard.add(key);
    return keyboard;

def get_entity_by_id(entities, id):
    for entity in entities:
        if entity.id == id:
            return entity
    return None;

def get_name(message): #отримуємо ім'я
    global name;
    name = message.text;
    order.set_user_name(name);
    bot.send_message(message.from_user.id, 'Номер телефону');
    bot.register_next_step_handler(message, get_phone);

def get_phone(message): #отримуємо номер телефону
    global phone;
    phone = message.text;
    order.set_user_phone(phone);
    batteries = dbctx.get_all_batteries()
    keyboard = get_keyboard(batteries);
    bot.send_message(message.from_user.id, 'Виберіть батарею з ціною', reply_markup=keyboard);

@bot.callback_query_handler(func=lambda call: True)
def get_battery(call): #отримуємо батарею
    print(f"call.data = {call.data}")
    id = int(call.data);
    battery = get_entity_by_id(batteries, id);
    order.set_battery(battery)
    invertors = dbctx.get_all_invertors()
    keyboard = get_keyboard(invertors);
    bot.send_message(call.message.chat.id, 'Виберіть інвертор з ціною', reply_markup=keyboard);

@bot.callback_query_handler(func=lambda call: True)
def get_invertor(call): #отримуємо інвертор
    print(f"call.data = {call.data}")
    id = int(call.data[0]);
    invertor = get_entity_by_id(invertors, id);
    order.set_invertor(invertor)

    bot.send_message(call.message.chat.id, f"""Ваше замовлення {order.UserName}. 
                     {order.Invertor.Name} - {order.Invertor.Price} \r\n
                     {order.Battery.Name} - {order.Battery.Price} ]r]n
                     Загальна сума - {order.Invertor.Price + order.Battery.Price}. \r\n
                     Чекайте на дзвінок за вказаним вами номером для підтвердження замовлення
                     """ );
    #bot.register_next_step_handler(message, get_battery);

bot.polling(none_stop=True, interval=0)