import os
import sys
import django
from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from environs import Env

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diary_bot.settings')
django.setup()

# Настройка Django
# from .models import Schoolkid, Parent, Teacher, Subject, Lesson, Mark, Chastisement, Commendation
from .utils import get_chastisements
from .helpers import chastisements


env = Env()
env.read_env()

TELEGRAM_BOT_TOKEN = env.str('BOT_TOKEN')
bot = TeleBot(TELEGRAM_BOT_TOKEN)



def main():

    @bot.message_handler(commands=['start'])
    def send(message):
        bot.reply_to(message, 'Привет! Используй /chastisements для просмотра замечаний.')

    @bot.message_handler(func=chastisements)
    def send_message(message):
        print(message)
        result = get_chastisements(f'@{message.chat.username}')
        bot.send_message(message.chat.id, result)

if __name__ == "__main__":
    main()
    print("Бот запущен")
    bot.polling()