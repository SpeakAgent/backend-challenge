from django.contrib import admin

from .forms import SchoolForm
from .models import School, Student, Teacher


class SchoolAdmin(admin.ModelAdmin):
    form = SchoolForm


admin.site.register(School, SchoolAdmin)


class StudentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Student, StudentAdmin)


class TeacherAdmin(admin.ModelAdmin):
    pass


admin.site.register(Teacher, TeacherAdmin)
