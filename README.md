# Телеграм-бот Электронный Дневник (Beta)

***Это Телеграм-бот электронного дневника написанный на `Django`, `Python` с использованием базы данных `SQLite3`***

### Роли и их возможности

*Люди добавляются в базу данных и обязательное поле которые должно быть у каждого участника это его юзернейм* (`@forexample`)

*Роль определяется по юзернейму, и каждая роль имеет свои кнопки, команды и возможности*

- `Ученик` - ученик, может получить:
  > - Информацию о боте
  > - Информацию о себе
  > - Расписание
  > - Оценки
  > - Похвалы
  > - Замечания от учителей
  > - Домашние задания
  > - Просматривать события в школе

- `Учитель` - учитель, классный руководитель и другие лица являющиеся администрацией школы имеют право:
    > - Все перечисленное в `Ученик`
    > - Добавлять домашнее задание
    > - Добавлять замечание
    > - Добавлять похвалу
    > - Добавлять событие
    > - Ставить оценки
    > - Составлять расписание

- `Родитель` - родитель, опекунд или другое доверенное лицо отвечающее за ученика:
    > - Все перечисленное в `Ученик`
    > - Выбрать про кого из своих детей посмотреть информацию

- `Неавторизованный` - человек, ребенок, гражданин которого нет в школе может:
  > - Посмотреть информацию про школу

*!СЕЙЧАС БОТ НАХОДИТСЯ В БЕТА ВЕРСИЙ И ФУНКЦИЙ УЧИТЕЛЯ И РОДИТЕЛЯ МОГУТ ПОКА БЫТЬ НЕДОСТУПНЫ!*

### Как запустить?

1. Открыть директорию проекта

2. Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

3. Выполнить миграций
```
python manage.py makemigrations
python manage,py migrate
```

4. Запустить бота
```
python -m bot.bot
```

### Переменные окружения

- BOT_TOKEN - Токен бота телеграм

Для того что бы скрипт запустился необходимо создать файл `.env` и туда вписать переменные окружения.

Пример:

```
BOT_TOKEN=bottoken123
```

### Над проектом работали ***Албариев Амиржан*** и ***Искаков Адилет***





