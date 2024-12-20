from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


user_states = {}

def about_bot(message):
    return message.text == 'О боте'

def about_me(message):
    return message.text == 'О себе'

def lesson_schedule(message):
    return message.text == 'Расписание'

def homework(message):
    return message.text == 'Домашние задания'

def marks(message):
    return message.text == 'Оценки'

def events(message):
    return message.text == 'События'

def commendations(message):
    return message.text == 'Похвалы'

def chastisements(message):
    return message.text == 'Замечания'

def teacher_beta(message):
    return message.text == 'Я учитель'

def without_role_beta(message):
    return message.text == 'Узнать про школу'

def create_reply_keyboard(role):
    
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    
    if role == 'schoolkid':
        
        btn1 = KeyboardButton('О боте')
        btn2 = KeyboardButton('О себе')
        btn3 = KeyboardButton('Расписание')
        btn4 = KeyboardButton('События')
        btn5 = KeyboardButton('Замечания')
        btn6 = KeyboardButton('Похвалы')
        btn7 = KeyboardButton('Домашние задания')
        btn8 = KeyboardButton('Оценки')

        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)

    elif role == 'teacher':

        btn1 = KeyboardButton('Я учитель')
        
        keyboard.add(btn1)

    else:

        btn1 = KeyboardButton('Узнать про школу')

    return keyboard
    
