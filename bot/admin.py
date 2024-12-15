from django.contrib import admin
from .models import (
    Schoolkid,
    Teacher,
    Subject,
    Lesson,
    Mark,
    Chastisement,
    Commendation,
    Parent,
    Homework
)


@admin.register(Schoolkid)
class SchoolkidAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'class_name', 'birthday', 'get_parent')
    search_fields = ('full_name', 'class_name')
    list_filter = ('class_name',)
    ordering = ('class_name',)

    def get_parent(self, obj):
        return ", ".join([parent.full_name for parent in obj.parents.all()])
    get_parent.short_description = 'Родители'


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birthday')
    search_fields = ('full_name',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('subject', 'teacher', 'group_letter', 'date', 'timeslot', 'room')
    search_fields = ('subject__title', 'teacher__full_name', 'room')
    list_filter = ('group_letter', 'date', 'timeslot')


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('points', 'schoolkid', 'subject', 'teacher', 'created')
    search_fields = ('schoolkid__full_name', 'subject__title')
    list_filter = ('subject', 'points')


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
    list_display = ('full_name', 'phone_number', 'email', 'telegram_id', 'get_children')
    search_fields = ('full_name', 'phone_number', 'email', 'telegram_id')

    def get_children(self, obj):
        return ", ".join([child.full_name for child in obj.children.all()])
    get_children.short_description = 'Дети'


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'group_letter', 'due_date')
    search_fields = ('title', 'subject__title', 'group_letter')
    list_filter = ('due_date', 'group_letter')