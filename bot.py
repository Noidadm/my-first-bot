import telebot
import os

# Mengambil token dari Environment Variable (biar aman)
API_TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

# Respon saat kamu ketik /start
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Halo! Aku bot buatan kamu. Apa yang bisa aku bantu?")

# Bot akan membalas chat apapun dengan kata-kata yang sama (Echo)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Kamu tadi bilang: {message.text}")

print("Bot sedang berjalan...")
bot.infinity_polling()
