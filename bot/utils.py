from .models import Schoolkid, Parent, Teacher, Subject, Lesson, Mark, Chastisement, Commendation, Event, Homework, ClassGroup
import django
import os
from django.shortcuts import get_object_or_404
from datetime import datetime

def get_user_role(tg_id):
    if get_object_or_404(Schoolkid, telegram_id=tg_id):
        return 'schoolkid'
    elif get_object_or_404(Parent, telegram_id=tg_id):
        return 'parent'
    elif get_object_or_404(Teacher, telegram_id=tg_id):
        return 'teacher'
    else:
        return None
    
def get_chastisements(tg_id):
    try:
        schoolkid = get_object_or_404(Schoolkid, telegram_id=tg_id)

    except:
    # Возвращаем более информативное сообщение или другую обработку
        return 'Не найдено'

    chastisements = Chastisement.objects.filter(schoolkid=schoolkid).order_by('-created')

    if not chastisements:
        return 'У вас нет замечаний'
    
    result = f'Ваши замечания \n'

    for chastisement in chastisements:
        result += f'Предмет: {chastisement.subject.title} \n'
        result += f'Учитель: {chastisement.teacher.full_name} \n'
        result += f'Дата: {chastisement.created} \n'
        result += f'Текст замечания: {chastisement.text} \n'
        result += '\n'
    
    return result

def get_commendations(tg_id):
    schoolkid = get_object_or_404(Schoolkid, telegram_id=tg_id)

    commendations = Commendation.objects.filter(schoolkid=schoolkid)

    if not commendations:
        return 'Вас не хвалили'
    
    result = f'Ваши похвалы \n'

    for commendation in commendations:
        result += f'Предмет: {commendation.subject.title} \n'
        result += f'Учитель: {commendation.teacher.full_name} \n'
        result += f'Дата: {commendation.created} \n'
        result += f'Текст похвалы: {commendation.text} \n'
    return result

def get_about_me(tg_id, role):

    result = 'Информация о вас\n \n'
    if role == 'teacher':
        teacher = get_object_or_404(Teacher, telegram_id=tg_id)
        result +=f'Роль: Учитель\n'
        result +=f'ФИО: {teacher.full_name}\n'
        result +=f'Дата рождения: {teacher.birthday}\n'
    elif role == 'schoolkid':
        schoolkid = get_object_or_404(Schoolkid, telegram_id=tg_id)
        result +=f'Роль: Ученик\n'
        result +=f'ФИО: {schoolkid.full_name}\n'
        result +=f'Дата рождения: {schoolkid.birthday}\n'
        result +=f'Класс: {schoolkid.class_group}\n'
    
    return result

def get_events():
    events = Event.objects.all()
    result = 'События в школе\n \n'
    
    for event in events:
        date = event.datetime.strftime("%d-%m-%Y %H:%M:%S")
        result +=f'Название события: {event.title}\n'
        result +=f'Дата проведения: {date}\n \n'
    return result

def get_marks(tg_id):
    schoolkid = get_object_or_404(Schoolkid, telegram_id=tg_id)
    marks = Mark.objects.filter(schoolkid=schoolkid)
    result = 'Ваши оценки\n \n'

    for mark in marks:
        result+=f'Оценка: {mark.points}]\n'
        result+=f'Учитель: {mark.teacher}\n'
        result+=f'Комментарий: {mark.teacher_note}\n'
        result+=f'Предмет: {mark.subject}\n'
        result+=f'Дата: {mark.created}\n \n'

    return result

def get_homework(tg_id):
    schoolkid = get_object_or_404(Schoolkid, telegram_id=tg_id)

    homeworks = Homework.objects.filter(class_group=schoolkid.class_group)

    result = 'Ваше домашнее задание\n\n'

    for homework in homeworks:
        result+=f'задание: {homework.title}\n'
        result+=f'Предмет: {homework.subject}\n'
        result+=f'Описание: {homework.description}\n'
        result+=f'Класс: {homework.class_group}\n\n'
    return result



        





    