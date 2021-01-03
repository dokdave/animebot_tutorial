import telebot
from telebot import types
import ani_main
import random

bot = telebot.TeleBot("663778064:AAEWkQB0BfqamVpOX3ipFfSUHaakBbDGCBE", parse_mode=None)

genres = list(ani_main.dict1.keys())

def main__(message):
	markup1 = types.ReplyKeyboardMarkup()
	f = types.KeyboardButton("/start")
	c = types.KeyboardButton("/help")
	markup1.row(f,c)
	msg2 = bot.send_message(message.chat.id, "Start or help?:", reply_markup=markup1)

@bot.message_handler(commands=['help'])
def main_2(message):
	bot.reply_to(message.chat.id, 'This is an introductory example bot to the library pyTelegramBotAPI')

@bot.message_handler(commands=['start'])
def main_(message):
	markup = types.ReplyKeyboardMarkup()
	markup_list = []
	for i in range(len(genres)):
		genre = types.KeyboardButton(genres[i])
		markup_list.append(genre)
	
		if len(markup_list) == 3:
			markup.row(markup_list[0], markup_list[1], markup_list[2])
			markup_list = []
			
	msg = bot.send_message(message.chat.id, "Choose the genre below:", reply_markup=markup)
	bot.register_next_step_handler(msg, genre_selector)
	
def genre_selector(message):
	if message.text in genres:
		link = ani_main.dict1[message.text]
		val1, val2 = ani_main.by_zhanr(message.text, link)
		
		try:
			new_list = random.sample(list(val1.keys()), 5)
		except:
			msg3 = bot.send_message(message, "No elements for this genre")
			bot.register_next_step_handler(msg3, main__)
		
		for name in new_list:
			bot.send_message(message.chat.id, name + ': ' + val1[name])
			
		msg = bot.reply_to(message, "Did I help you?")
		bot.register_next_step_handler(msg, finish_continue)

def finish_continue(message):
	markup1 = types.ReplyKeyboardMarkup()
	f = types.KeyboardButton("Finish")
	c = types.KeyboardButton("Continue")
	markup1.row(f,c)
	msg2 = bot.send_message(message.chat.id, "Finish or continue?:", reply_markup=markup1)
	bot.register_next_step_handler(msg2, finish_continue2)

def finish_continue2(message):
	if message.text == 'Finish':
		bot.send_message(message.chat.id, "Thanks for using me)))")
	elif message.text == 'Continue':
		msg2 = bot.send_message(message, "Let's go")
		bot.register_next_step_handler(msg2, main__)
	else:
		msg = bot.send_message(message.chat.id, "Choose one of them:")
		bot.register_next_step_handler(msg, finish_continue2)
		
@bot.message_handler(commands=['hi', 'Hi'])
def send_welcome(message):
	bot.reply_to(message, "Hi, how are you doing?")


@bot.message_handler(commands=['stp'])
def stop_command(message):
  print("ok")
  bot.stop_polling()

bot.polling()