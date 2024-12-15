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
    entry_year = models.IntegerField('Год начала обучения', null=True)
    class_name = models.CharField('Класс', max_length=10, blank=True)  # Новое поле
    telegram_id = models.CharField('Telegram ID', max_length=100, default='', blank=True)

    # Связь с родителями
    parents = models.ManyToManyField('Parent', verbose_name='Родители', related_name='children', blank=True)

    def __str__(self):
        return f'{self.full_name} {self.class_name}'

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


class Lesson(models.Model):
    """Один урок в расписании занятий."""
    TIMESLOTS_SCHEDULE = [
        '8:00-8:40',
        '8:50-9:30',
        '9:40-10:20',
        '10:35-11:15',
        '11:25-12:05'
    ]
    group_letter = models.CharField('Литера класса', max_length=1, db_index=True)
    subject = models.ForeignKey(
        Subject,
        null=True,
        verbose_name='Предмет',
        on_delete=models.CASCADE)
    teacher = models.ForeignKey(
        Teacher,
        null=True,
        verbose_name='Учитель',
        on_delete=models.CASCADE)
    timeslot = models.IntegerField(
        'Слот',
        db_index=True,
        help_text='Номер слота в расписании уроков на этот день.')
    room = models.CharField(
        'Класс',
        db_index=True,
        max_length=50,
        help_text='Класс где проходят занятия.')
    date = models.DateField('Дата', db_index=True)

    def __str__(self):
        return f'{self.subject.title} {self.group_letter}'


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
    group_letter = models.CharField(
        'Литера класса',
        max_length=1,
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
        return f'{self.title} - {self.subject.title}'

    class Meta:
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Домашние задания'