from django.shortcuts import render
from django.views.generic import ListView

from .models import Student


# Class Based View
class StudentView(ListView):
    queryset = Student.objects.filter(grade='A')
    context_object_name = 'students'
    template_name = 'student_list.html'


# Function Based View
# def StudentView(request):
#     student_list = Student.objects.filter(grade='A')
#     return render(request, 'student_list.html', {'students': student_list})
