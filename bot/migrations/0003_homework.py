# Generated by Django 5.0.6 on 2024-12-14 21:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_alter_parent_options_alter_schoolkid_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название задания')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('due_date', models.DateField(verbose_name='Срок выполнения')),
                ('schoolkid', models.ManyToManyField(blank=True, related_name='homeworks', to='bot.schoolkid', verbose_name='Ученики')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.subject', verbose_name='Предмет')),
            ],
            options={
                'verbose_name': 'Домашнее задание',
                'verbose_name_plural': 'Домашние задания',
            },
        ),
    ]
