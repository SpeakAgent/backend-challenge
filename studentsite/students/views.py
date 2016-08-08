from django.shortcuts import render
from django.views.generic import ListView

from .models import Student
from .serializers import StudentSerializer

from rest_framework.viewsets import ReadOnlyModelViewSet


# Class Based View
class StudentView(ListView):
    queryset = Student.objects.filter(grade='K')
    context_object_name = 'students'
    template_name = 'student_list.html'


# Function Based View
# def StudentView(request):
#     student_list = Student.objects.filter(grade='K')
#     return render(request, 'student_list.html', {'students': student_list})


# Api calls
class StudentViewSet(ReadOnlyModelViewSet):
    """
    ###Retrieve student by id
    - ####Example:
        *  #####Student by id: [/api/students/1](/api/students/1)
    ---
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
