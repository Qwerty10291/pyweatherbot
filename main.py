import telebot
bot = telebot.TeleBot('1253872655:AAGmMEGxoiQ67aa8g_Rj3TNMeXmhQKpg9N8')
@bot.message_handler(content_types=['text'])
def send_text(message):
	bot.send_message(message.chat.id, message.text)
bot.polling()
