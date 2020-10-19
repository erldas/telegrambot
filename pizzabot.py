import telebot
from telebot import types
import csv 


bot = telebot.TeleBot("1117992682:AAFS69DnEAMtXsxk3WCZhza6p16n5caxRKs")

entry = {}


order_keyboard = types.InlineKeyboardMarkup(row_width=1)
btn1 = types.InlineKeyboardButton("Пицца 🍕", callback_data='1')
btn2 = types.InlineKeyboardButton("Закуски 🍟", callback_data='2')
btn3 = types.InlineKeyboardButton("Салаты 🥗", callback_data='3')
btn4 = types.InlineKeyboardButton("Напитки 🍹", callback_data='4')
btn5 = types.InlineKeyboardButton("Соусы 🥫", callback_data='5')
btn6 = types.InlineKeyboardButton("Мои заказы", callback_data="show")
order_keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6)

@bot.message_handler(commands=['start', 'go'])
def start_(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, text="Добро пожаловать " + message.from_user.first_name + " в наш уютный ресторан! Выберите что вы будете заказывать 😋 /menu")

@bot.message_handler(commands=['menu'])
def order_(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, text='Выберите что вы бы хотели заказать?', reply_markup=order_keyboard)

@bot.callback_query_handler(func = lambda c: True )
def inline_(c):
    if c.data == '1':
        pizza_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        p1 = types.KeyboardButton('Маргарита')
        p2 = types.KeyboardButton('Пепперони')
        p3 = types.KeyboardButton('Мексиканка')
        p4 = types.KeyboardButton('4 сыра')
        p5 = types.KeyboardButton('Чили')
        p6 = types.KeyboardButton('Мясная')
        p7 = types.KeyboardButton('Гасконская')
        p8 = types.KeyboardButton('Тропиканка')
        p9 = types.KeyboardButton('Охотничья')
        p10 = types.KeyboardButton('Райские грезы')
        pizza_keyboard.add(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
        msg1 = bot.send_message(c.message.chat.id, text='Какую пиццу хотите заказать?', reply_markup=pizza_keyboard )
        bot.register_next_step_handler(msg1, order_pizza)



    if c.data == '2':
        chat_id = c.message.chat.id
        zakuski_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        z1 = types.KeyboardButton('Пири пири Попперс')
        z2 = types.KeyboardButton('Сырные палочки')
        z3 = types.KeyboardButton('Картофель-фри')
        z4 = types.KeyboardButton('Чикен Попперс')
        z5 = types.KeyboardButton('Куриные Крылышки')
        z6 = types.KeyboardButton('Луковые кольца')
        zakuski_keyboard.add(z1, z2, z3, z4, z5, z6)
        msg2 = bot.send_message(c.message.chat.id, 'Какую закуску хотите заказать?',reply_markup=zakuski_keyboard)
        bot.register_next_step_handler(msg2, order_zakuski)

    if c.data == '3':
        chat_id = c.message.chat.id
        salad_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        s1 = types.KeyboardButton('Цезарь')
        s2 = types.KeyboardButton('Свежий')
        s3 = types.KeyboardButton('Оливье')
        s4 = types.KeyboardButton('Сельдь под шубой')
        s5 = types.KeyboardButton('Ленивые язычки')
        s6 = types.KeyboardButton('Греческий')
        salad_keyboard.add(s1, s2, s3, s4, s5, s6) 
        msg3 = bot.send_message(c.message.chat.id, 'Какой салат хотите заказать?', reply_markup=salad_keyboard)
        bot.register_next_step_handler(msg3, order_salad)

    if c.data == '4':
        chat_id = c.message.chat.id
        drinks_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        d1 = types.KeyboardButton('Спрайт')
        d2 = types.KeyboardButton('Пина Колада')
        d3 = types.KeyboardButton('Айс Тии')
        d4 = types.KeyboardButton('Кока-Кола')
        d5 = types.KeyboardButton('Свежевжитый Апельсиновый Сок')
        d6 = types.KeyboardButton('Вода')
        drinks_keyboard.add(d1, d2, d3, d4, d5, d6)
        msg4 = bot.send_message(c.message.chat.id, 'Что желаете выпить?', reply_markup=drinks_keyboard)
        bot.register_next_step_handler(msg4, order_drink)

    if c.data == '5':
        chat_id = c.message.chat.id
        souses_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        ss1 = types.KeyboardButton('Острый')
        ss2 = types.KeyboardButton('Грейви')
        ss3 = types.KeyboardButton('Хумус')
        ss4 = types.KeyboardButton('Горчичный')
        ss5 = types.KeyboardButton('Кетчуп')
        ss6 = types.KeyboardButton('Майонез')
        souses_keyboard.add(ss1, ss2, ss3, ss4, ss5, ss6)
        msg5 = bot.send_message(c.message.chat.id, 'Какой соус хотите заказать?',reply_markup=souses_keyboard)
        bot.register_next_step_handler(msg5, order_sous)

    if c.data == "show":
        chat_id = c.message.chat.id
        show_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        btn = types.KeyboardButton('Show Order')
        show_keyboard.add(btn)
        bot.send_message(chat_id, text=otpravka())



def order_pizza(message):
    chat_id = message.chat.id
    entry['Pizza:'] = "Вы заказали пиццу:" +  message.text
    msg1 = bot.send_message(message.chat.id, text='Cпасибо за заказ, что-нибудь еще?', reply_markup=order_keyboard)
    bot.register_next_step_handler(msg1, get_finish)


def order_zakuski(message):
    chat_id = message.chat.id
    entry['Zakuski:'] = "Закуски:" + message.text
    msg2 = bot.send_message(message.chat.id, 'Cпасибо за заказ,что-нибудь еще?', reply_markup=order_keyboard)
    bot.register_next_step_handler(msg2, get_finish)
    

def order_salad(message):
    chat_id = message.chat.id
    entry['Salad:'] = "Салат:" + message.text
    msg3 = bot.send_message(message.chat.id, 'Cпасибо за заказ, что-нибудь еще?',reply_markup=order_keyboard)
    bot.register_next_step_handler(msg3, get_finish)

def order_drink(message):
    chat_id = message.chat.id
    entry['Drinks:'] = "Попить:" + message.text
    msg4 = bot.send_message(message.chat.id, 'Cпасибо за заказ, что-нибудь еще?',reply_markup=order_keyboard)
    bot.register_next_step_handler(msg4, get_finish)

def order_sous(message):
    chat_id = message.chat.id
    entry['Sous:'] = "Соус:" + message.text
    msg5 = bot.send_message(message.chat.id, 'Cпасибо!, ваш заказ выполняется, ожидайте!',reply_markup=order_keyboard)
    bot.register_next_step_handler(msg5, get_finish)
    



def get_finish(message):
    chat_id = message.chat.id
    show_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    btn = types.KeyboardButton('Show Order')
    show_keyboard.add(btn)
    file_name = 'order.csv'

    with open(file_name, 'w+', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=' ')
        writer.writerow((message.from_user.first_name, entry.get('Pizza:'), entry.get('Zakuski:'), entry.get('Salad:'), entry.get('Drinks:'), entry.get('Sous:')))

def otpravka():
    with open('order.csv', 'r+', encoding="utf-8") as send:
        group = send.read()
        return group 


@bot.message_handler(commands=['show'])
def group(message):

    chat_id = message.chat.id
    bot.send_message(chat_id, text=otpravka())

@bot.message_handler(content_types=['text'])
def text_(message):  
    chat_id = message.chat.id

    if message.text == "Спасибо":
        bot.reply_to(message, text="Спасибо Вам, ждем вас еще 🤩")
    elif message.text == "Скидка":
        bot.reply_to(message, text="При заказе двух пиц, литр Колы бесплатно")
    else:
        bot.reply_to(message, text="Извините, я вас не понимаю 😔" )
        bot.send_sticker(chat_id, "CAACAgIAAxkBAAEBHEVfIA3pvFh8uEa0tWJ3m-nD96vD8QACcwMAAs9fiwfCgv-3CcoXgBoE")



bot.polling()