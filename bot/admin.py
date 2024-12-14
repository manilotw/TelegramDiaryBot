from django.contrib import admin
from .models import (
    Schoolkid,
    Teacher,
    Subject,
    Lesson,
    Mark,
    Chastisement,
    Commendation,
    Parent
)


@admin.register(Schoolkid)
class SchoolkidAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'year_of_study', 'group_letter', 'entry_year', 'birthday')
    search_fields = ('full_name', 'group_letter')
    list_filter = ('year_of_study', 'group_letter')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birthday')
    search_fields = ('full_name',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'year_of_study')
    search_fields = ('title',)
    list_filter = ('year_of_study',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('subject', 'teacher', 'year_of_study', 'group_letter', 'date', 'timeslot', 'room')
    search_fields = ('subject__title', 'teacher__full_name', 'room')
    list_filter = ('year_of_study', 'group_letter', 'date', 'timeslot')


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('points', 'schoolkid', 'subject', 'teacher', 'created')
    search_fields = ('schoolkid__full_name', 'subject__title', 'teacher__full_name')
    list_filter = ('points', 'created')


@admin.register(Chastisement)
class ChastisementAdmin(admin.ModelAdmin):
    list_display = ('text', 'schoolkid', 'subject', 'teacher', 'created')
    search_fields = ('schoolkid__full_name', 'text', 'subject__title', 'teacher__full_name')
    list_filter = ('created',)


@admin.register(Commendation)
class CommendationAdmin(admin.ModelAdmin):
    list_display = ('text', 'schoolkid', 'subject', 'teacher', 'created')
    search_fields = ('schoolkid__full_name', 'text', 'subject__title', 'teacher__full_name')
    list_filter = ('created',)

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'email', 'telegram_id')
    search_fields = ('full_name', 'phone_number', 'email', 'telegram_id')