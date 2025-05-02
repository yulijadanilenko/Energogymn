
import telebot

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я ЭнергоБот. Готов помогать экономить энергию и делиться новостями.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Я получил твоё сообщение: " + message.text)

bot.polling()
