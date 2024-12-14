# Generated by Django 5.0.6 on 2024-12-14 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schoolkid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('birthday', models.DateField(null=True, verbose_name='день рождения')),
                ('entry_year', models.IntegerField(null=True, verbose_name='год начала обучения')),
                ('year_of_study', models.IntegerField(null=True, verbose_name='год обучения')),
                ('group_letter', models.CharField(blank=True, max_length=1, verbose_name='литера класса')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='название')),
                ('year_of_study', models.IntegerField(db_index=True, null=True, verbose_name='год обучения')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('birthday', models.DateField(null=True, verbose_name='день рождения')),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(verbose_name='оценка')),
                ('teacher_note', models.TextField(blank=True, verbose_name='комментарий')),
                ('created', models.DateField(verbose_name='дата')),
                ('schoolkid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.schoolkid', verbose_name='ученик')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.subject', verbose_name='предмет')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.teacher', verbose_name='учитель')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_of_study', models.IntegerField(db_index=True)),
                ('group_letter', models.CharField(db_index=True, max_length=1, verbose_name='литера класса')),
                ('timeslot', models.IntegerField(db_index=True, help_text='Номер слота в расписании уроков на этот день.', verbose_name='слот')),
                ('room', models.CharField(db_index=True, help_text='Класс где проходят занятия.', max_length=50, verbose_name='класс')),
                ('date', models.DateField(db_index=True, verbose_name='дата')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.subject', verbose_name='предмет')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.teacher', verbose_name='учитель')),
            ],
        ),
        migrations.CreateModel(
            name='Commendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='похвала')),
                ('created', models.DateField(db_index=True, verbose_name='дата')),
                ('schoolkid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.schoolkid', verbose_name='ученик')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bot.subject', verbose_name='предмет')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.teacher', verbose_name='учитель')),
            ],
        ),
        migrations.CreateModel(
            name='Chastisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='замечание')),
                ('created', models.DateField(db_index=True, verbose_name='дата')),
                ('schoolkid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.schoolkid', verbose_name='ученик')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bot.subject', verbose_name='предмет')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.teacher', verbose_name='учитель')),
            ],
        ),
    ]
