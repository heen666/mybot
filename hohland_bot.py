import config
import telebot
import random
import time

# Токен бота (Связь с ботом)
bot = telebot.TeleBot(config.TOKEN)

# Команды
# Приветствие
@bot.message_handler(commands = ['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'Привет, я ХохландБот мои создатели организация Hohland. Чтобы узнать, что я умею пропиши "/help"')


# Помощь по командам
@bot.message_handler(commands = ['help'])
def help_message(message):
	bot.send_message(message.chat.id, 'Это мои команды:\n1. /roll - выдает случайное число от 1 - 100\n2. /coin or /flip - подбрасывает монетку\n3. /compliment - делает вам приятно =)\n4.  ')


# Ролл от 1 до 100
@bot.message_handler(commands = ['roll'])
def roll_message(message):
	roll_number = random.randint(1, 100)
	bot.reply_to(message, 'Твое число: '+str(roll_number))


# Коин флип
@bot.message_handler(commands = ['coin', 'flip'])
def coin_message(message):
	bot.send_message(message.chat.id, 'Подбрасываю монетку')
	second = 4
	for timer in range (3):
		second -= 1
		bot.send_message(message.chat.id, str(second))
		time.sleep(1)
	coin = random.randint(1, 2)
	if coin == 1:
		bot.send_message(message.chat.id, 'Выпал орёл')
	else:
		bot.send_message(message.chat.id, 'Выпала решка')


# Комплименты
@bot.message_handler(commands = ['compliment'])
def compliment_message(message):
	compliment_number = random.randint(1, 5)
	if compliment_number == 1:
		bot.reply_to(message, 'Вы красивы! 😍')
	elif compliment_number == 2:
		bot.reply_to(message, 'Вы прекрасны! 👑')
	elif compliment_number == 3:
		bot.reply_to(message, 'Вы невероятны! ✨')
	elif compliment_number == 4:
		bot.reply_to(messagem, 'Кажется, я влюбляюсь! 💕')
	elif compliment_number == 5:
		bot.reply_to(message, 'Вы супер! 👍')


# Контент типа (текст)
@bot.message_handler(content_types = 'text')
# Ответ на "Слава Украине"
def send_text(message):
	bad_words_score = 0
	if message.text.lower() == 'слава украине':
		bot.send_message(message.chat.id, 'Героям слава!')
	elif message.text.lower() == 'слава нации':
		bot.send_message(message.chat.id, 'Смерть ворогам!')

# Счётчик запретных слов



# Чтобы наш бот не выключался сразу
bot.polling(none_stop = True)