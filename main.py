import telebot
import datetime

bot = telebot.TeleBot('token') #вписать токен бота

@bot.message_handlers(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет!")
    bot.send_message(message.chat.id, f'Я пробил информацию:\n\n'
                                      f'Id чата: {message.chat.id}\n'
                                      f'Id пользователя: {message.from_user.id}\n'
                                      f'Имя: {message.from_user.first_name}\n'
                                      f'Фамилия: {message.from_user.last_name}\n'
                                      f'Псевдоним: {message.from_user.username}\n\n'
                                      f'Текст сообщения: {message.text}')

@bot.message_handlers(commands=['time'])
def time(message):
    date = message.date + 10800  # Прибавляем 3 часа (в секундах) к времени по UTC и получаем время по МСК
    bot.send_message(message.chat.id, "Время, когда вы отправили это сообщение: " + str(datetime.datetime.utcfromtimestamp(date)))

@bot.message_handlers(func = lambda message: True) #эта лямбда помогает отвечать на все сообщения
def time(message):
    bot.reply_to(message, f"Вы отправили сообщение: {message}") #reply_to отвечает на отправленное сообщение

@bot.message_handler(func=lambda m: m.text == 'SnorovkaSchool') #эта лямбда помогает отвечать только на определенные сообщения
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()