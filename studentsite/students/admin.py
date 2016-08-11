from django.contrib import admin

from students.models import School, Student, Teacher


class SchoolAdmin(admin.ModelAdmin):
    pass


admin.site.register(School, SchoolAdmin)


class StudentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Student, StudentAdmin)


class TeacherAdmin(admin.ModelAdmin):
    pass


admin.site.register(Teacher, TeacherAdmin)
