from django.contrib import admin

from students.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'grade', 'date_of_birth')

admin.site.register(Student, StudentAdmin)
