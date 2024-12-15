from django.db import models


class Parent(models.Model):
    """Родитель."""
    full_name = models.CharField('ФИО', max_length=200)
    phone_number = models.CharField('Номер телефона', max_length=20, blank=True)
    email = models.EmailField('Электронная почта', blank=True)
    telegram_id = models.CharField('Telegram ID', max_length=100, default='', blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Родитель'
        verbose_name_plural = 'Родители'


class Schoolkid(models.Model):
    """Ученик."""
    full_name = models.CharField('ФИО', max_length=200)
    birthday = models.DateField('День рождения', null=True)
    class_name = models.CharField('Класс', max_length=10, blank=True)  # Новое поле
    telegram_id = models.CharField('Telegram ID', max_length=100, default='', blank=True)

    # Связь с родителями
    parents = models.ManyToManyField('Parent', verbose_name='Родители', related_name='children', blank=True)

    def __str__(self):
        return f'{self.full_name} {self.class_name}'

    class_group = models.ForeignKey(
        'ClassGroup',
        verbose_name='Класс',
        null=True,
        on_delete=models.SET_NULL,
        related_name='students'
    )

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def get_average_marks(self):
        """Рассчитать средний балл ученика по всем предметам."""
        marks = Mark.objects.filter(schoolkid=self)
        if marks.exists():
            return marks.aggregate(average=models.Avg('points'))['average']
        return None

    def get_marks_by_subject(self):
        """Статистика оценок по предметам."""
        marks = Mark.objects.filter(schoolkid=self)
        return marks.values('subject__title').annotate(average=models.Avg('points'))



class Teacher(models.Model):
    """Учитель."""
    full_name = models.CharField('ФИО', max_length=200)
    birthday = models.DateField('День рождения', null=True)
    telegram_id = models.CharField('Telegram ID', max_length=100, default='', blank=True)

    def __str__(self):
        return self.full_name


class Subject(models.Model):
    """Предмет: математика, русский язык и пр."""
    title = models.CharField('Название', max_length=200)

    def __str__(self):
        return self.title


from django.db import models

class Lesson(models.Model):
    """Один урок в расписании занятий."""

    # Класс, которому назначен урок
    class_group = models.ForeignKey(
        'ClassGroup',
        null=True,
        verbose_name='Класс',
        on_delete=models.CASCADE
    )

    # Позволяет выбрать несколько предметов для урока
    subjects = models.ManyToManyField(
        'Subject',  # Ссылка на модель Subject, которая хранит предметы
        verbose_name='Предметы',
        related_name='lessons',
        help_text='Предметы, которые будут изучаться на этом уроке.'
    )


    def __str__(self):
        subject_titles = ', '.join([subject.title for subject in self.subjects.all()])
        return f'{self.class_group} | {subject_titles} '

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'




class Mark(models.Model):
    """Оценка, поставленная учителем ученику."""
    points = models.IntegerField('Оценка')
    teacher_note = models.TextField('Комментарий', blank=True)
    created = models.DateField('Дата')
    schoolkid = models.ForeignKey(
        Schoolkid,
        verbose_name='Ученик',
        on_delete=models.CASCADE)
    subject = models.ForeignKey(
        Subject,
        verbose_name='Предмет',
        on_delete=models.CASCADE)
    teacher = models.ForeignKey(
        Teacher,
        verbose_name='Учитель',
        on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.points} {self.schoolkid.full_name}'


class Chastisement(models.Model):
    """Запись с замечанием от учителя ученику."""
    text = models.TextField('Замечание')
    created = models.DateField('Дата', db_index=True)
    schoolkid = models.ForeignKey(
        Schoolkid,
        verbose_name='Ученик',
        on_delete=models.CASCADE)
    subject = models.ForeignKey(
        Subject,
        verbose_name='Предмет',
        null=True,
        on_delete=models.SET_NULL)
    teacher = models.ForeignKey(
        Teacher,
        verbose_name='Учитель',
        on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.schoolkid.full_name}'


class Commendation(models.Model):
    """Запись с похвалой от учителя ученику."""
    text = models.TextField('Похвала')
    created = models.DateField('Дата', db_index=True)
    schoolkid = models.ForeignKey(
        Schoolkid,
        verbose_name='Ученик',
        on_delete=models.CASCADE)
    subject = models.ForeignKey(
        Subject,
        verbose_name='Предмет',
        null=True,
        on_delete=models.SET_NULL)
    teacher = models.ForeignKey(
        Teacher,
        verbose_name='Учитель',
        on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.schoolkid.full_name}'

class ClassGroup(models.Model):
    """Модель для представления классов, например, 11А, 10Б."""
    year = models.IntegerField('Год обучения')  # Например, 10, 11
    letter = models.CharField('Литера', max_length=1)  # Например, А, Б
    teacher = models.ForeignKey(
        'Teacher',
        verbose_name='Классный руководитель',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f'{self.year}{self.letter}'

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
        unique_together = ('year', 'letter')  # Уникальность класса (например, 10А)

class Homework(models.Model):
    """Домашнее задание."""
    title = models.CharField('Название задания', max_length=255)
    description = models.TextField('Описание', blank=True)
    due_date = models.DateField('Срок выполнения')
    subject = models.ForeignKey(
        Subject,
        verbose_name='Предмет',
        on_delete=models.CASCADE
    )
    class_group = models.ForeignKey(
        'ClassGroup',
        verbose_name='Класс',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text='Класс, которому назначено задание'
    )
    schoolkids = models.ManyToManyField(
        Schoolkid,
        verbose_name='Ученики',
        related_name='homeworks',
        blank=True,
        help_text='Ученики, если задание задается не всему классу'
    )

    def __str__(self):
        return f'{self.title} - {self.subject.title} ({self.class_group})'

    class Meta:
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Домашние задания'

class Event(models.Model):
    """Модель для представления события (мероприятия)."""
    title = models.CharField(
        'Название события',
        max_length=200,
        help_text='Краткое название мероприятия.'
    )
    description = models.TextField(
        'Описание события',
        blank=True,
        help_text='Описание мероприятия, например, тематика или цель.'
    )
    datetime = models.DateTimeField(
        'Дата и время',
        help_text='Дата и время начала события.'
    )
    location = models.CharField(
        'Место проведения',
        max_length=200,
        help_text='Где будет проходить мероприятие (например, актовый зал).'
    )
    class_group = models.ManyToManyField(
        'ClassGroup',
        verbose_name='Классы',
        blank=True,
        help_text='Классы, которые участвуют в мероприятии.'
    )

    def __str__(self):
        return f'{self.title} | {self.datetime} | {self.location}'

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        ordering = ['datetime']
