from django.contrib import admin

from .models import Student, Teacher, School


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'grade', 'date_of_birth')


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
