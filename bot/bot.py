import os
import sys
import django
from telebot import TeleBot
from environs import Env

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diary_bot.settings')
django.setup()

# Настройка Django
# from .models import Schoolkid, Parent, Teacher, Subject, Lesson, Mark, Chastisement, Commendation
from .utils import get_chastisements, get_about_me, get_commendations, get_events, get_homework, get_marks, get_user_role, get_scedule
from .helpers import chastisements, about_me, about_bot, lesson_schedule, homework, marks, commendations, create_reply_keyboard, events, teacher_beta, without_role_beta


env = Env()
env.read_env()

TELEGRAM_BOT_TOKEN = env.str('BOT_TOKEN')
bot = TeleBot(TELEGRAM_BOT_TOKEN)



def main():

    @bot.message_handler(commands=['start'])
    def send(message):
        keyboard = create_reply_keyboard(get_user_role(f'@{message.chat.username}'))
        bot.reply_to(message, 'Hi', reply_markup=keyboard)

    @bot.message_handler(func=chastisements)
    def send_chastisements(message):

        result = get_chastisements(f'@{message.chat.username}')
        bot.send_message(message.chat.id, result)

    @bot.message_handler(func=commendations)
    def send_commendations(message):

        result = get_commendations(f'@{message.chat.username}')
        bot.send_message(message.chat.id, result)

    @bot.message_handler(func=homework)
    def send_homework(message):

        result = get_homework(f'@{message.chat.username}')
        bot.send_message(message.chat.id, result)
    
    @bot.message_handler(func=about_bot)
    def send_about_bot(message):

        result = 'Адик и Амирж сделали бота ратата'
        bot.send_message(message.chat.id, result)

    @bot.message_handler(func=about_me)
    def send_about_me(message):

        result = get_about_me(f'@{message.chat.username}', get_user_role(f'@{message.chat.username}'))
        bot.send_message(message.chat.id, result)

    @bot.message_handler(func=marks)
    def send_marks(message):

        result = get_marks(f'@{message.chat.username}')
        bot.send_message(message.chat.id, result)

    @bot.message_handler(func=events)
    def send_event(message):

        result = get_events()
        bot.send_message(message.chat.id, result)
    
    @bot.message_handler(func=teacher_beta)
    def beta_teacher(message):
        result = 'Вы учитель? Это большая честь и отвественность, но для вас самое интересное будет попозже'
        bot.send_message(message.chat.id, result)

    @bot.message_handler(func=without_role_beta)
    def beta_teacher(message):
        result = 'Информация про нашу иновационную школу появиться скоро!'
        bot.send_message(message.chat.id, result)    

    @bot.message_handler(func=lesson_schedule)
    def send_schedule(message):
        result = get_scedule(f'@{message.chat.username}')
        bot.send_message(message.chat.id)

if __name__ == "__main__":
    main()
    print("Бот запущен")
    bot.polling()