import telebot


token = ''
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def about(message):
	bot.send_message(message.chat.id, 'Привет! Это обычный детектор рикрол ссылок!')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if "dQw4w9WgXcQ" in message.text:
        bot.send_message(message.chat.id, '🚨 Рикролл ссылка обнаружена!')

    elif "LLFhKaqnWwk" in message.text:
        bot.send_message(message.chat.id, '🚨 Рикролл ссылка обнаружена!')

    elif "CAZ8kTQ49c8" in message.text:
        bot.send_message(message.chat.id, '🚨 Рикролл ссылка обнаружена!')

    elif "GtL1huin9EE" in message.text:
        bot.send_message(message.chat.id, '🚨 Рикролл ссылка обнаружена!')

    elif "eM9FjdBvhOU" in message.text:
        bot.send_message(message.chat.id, '🚨 Рикролл ссылка обнаружена!')


bot.polling()
