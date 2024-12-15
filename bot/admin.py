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
    Homework,
    ClassGroup,
    Event

)


@admin.register(Schoolkid)
class SchoolkidAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'class_group', 'birthday', 'get_parent')
    search_fields = ('full_name', 'class_group__year', 'class_group__letter')
    list_filter = ('class_group__year', 'class_group__letter')
    ordering = ('class_group__year', 'class_group__letter', 'full_name')

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
    """Админка для модели Lesson (Урок)."""
    list_display = ('datetime', 'class_group', 'subject', 'teacher', 'room', 'timeslot')
    list_filter = ('datetime', 'class_group', 'subject', 'teacher', 'room', 'timeslot')
    search_fields = ('subject__title', 'teacher__name', 'room', 'class_group__year', 'class_group__letter')
    ordering = ('datetime', 'timeslot')
    date_hierarchy = 'datetime'  # Удобная навигация по датам


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
    """Админка для домашних заданий."""
    list_display = ('title', 'subject', 'class_group', 'due_date')
    search_fields = ('title', 'subject__title', 'class_group__year', 'class_group__letter')
    list_filter = ('due_date', 'subject', 'class_group')

    filter_horizontal = ('schoolkids',)  # Удобный выбор учеников через ManyToMany


@admin.register(ClassGroup)
class ClassGroupAdmin(admin.ModelAdmin):
    """Админка для классов."""
    list_display = ('year', 'letter', 'teacher', 'get_student_count')
    search_fields = ('year', 'letter', 'teacher__full_name')
    list_filter = ('year', 'letter')
    ordering = ('year', 'letter')

    def get_student_count(self, obj):
        """Количество учеников в классе."""
        return obj.students.count()
    get_student_count.short_description = 'Количество учеников'

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Админка для модели Event (Событие)."""
    list_display = ('title', 'datetime', 'location')
    list_filter = ('datetime', 'location', 'class_group')
    search_fields = ('title', 'location', 'class_group__year', 'class_group__letter')
    ordering = ('datetime',)


