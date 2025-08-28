

from transliterate import to_cyrillic,to_latin
import telebot
TOKEN='8174749200:AAF9CxhzH5CfU2s7Hs2PFWTs9wBaD2U1oc0'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	javob = 'Assalomu Alaykum, Xush kelibsiz!'
	javob += '\nMatn kiritng:'
	bot.reply_to(message,javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	msg = message.text
	javob = lambda msg: to_cyrillic(msg)  if  msg.isascii() else to_latin(msg)

	bot.reply_to(message, javob(msg))

bot.infinity_polling()

matn = input("Matn kiriting:")

if matn.isascii():
	print(to_cyrillic(matn))
else:
	print(to_latin(matn))