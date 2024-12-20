# Generated by Django 5.0.6 on 2024-12-15 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0010_remove_lesson_date_lesson_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Краткое название мероприятия.', max_length=200, verbose_name='Название события')),
                ('description', models.TextField(blank=True, help_text='Описание мероприятия, например, тематика или цель.', verbose_name='Описание события')),
                ('datetime', models.DateTimeField(help_text='Дата и время начала события.', verbose_name='Дата и время')),
                ('location', models.CharField(help_text='Где будет проходить мероприятие (например, актовый зал).', max_length=200, verbose_name='Место проведения')),
                ('class_group', models.ManyToManyField(blank=True, help_text='Классы, которые участвуют в мероприятии.', to='bot.classgroup', verbose_name='Классы')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
                'ordering': ['datetime'],
            },
        ),
    ]
