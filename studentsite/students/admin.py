from django.contrib import admin

from students.models import Student
from students.models import School
from students.models import Teacher

class StudentAdmin(admin.ModelAdmin):
    pass

class TeacherAdmin(admin.ModelAdmin):
    pass

class SchoolAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student, StudentAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Teacher, TeacherAdmin)
