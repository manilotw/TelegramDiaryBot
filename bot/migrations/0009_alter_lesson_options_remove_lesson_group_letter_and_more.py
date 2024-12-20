# Generated by Django 5.0.6 on 2024-12-15 08:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0008_remove_homework_group_letter_homework_class_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'Урок', 'verbose_name_plural': 'Уроки'},
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='group_letter',
        ),
        migrations.AddField(
            model_name='lesson',
            name='class_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.classgroup', verbose_name='Класс'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='room',
            field=models.CharField(db_index=True, help_text='Кабинет, где проходят занятия.', max_length=50, verbose_name='Кабинет'),
        ),
    ]
