import telebot

bot = telebot.TeleBot("7396118470:AAGbfQGQ5wzkUOFrA6VGTFqeH92_t3FdzTc")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')


@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, 'Сделал студент Б9123-01.03.02 ИИ Житинёв Иван')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '/info - информация о создателе бота')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)


bot.infinity_polling()