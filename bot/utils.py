from .models import Schoolkid, Parent, Teacher, Subject, Lesson, Mark, Chastisement, Commendation
import django
import os
from django.shortcuts import get_object_or_404


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





    