from django.shortcuts import render
from django.views.generic import ListView

from .models import Student
from .serializers import StudentSerializer

from rest_framework.viewsets import ReadOnlyModelViewSet


# Class Based View
class StudentView(ListView):
    context_object_name = 'data'
    template_name = 'student_list.html'

    def get_queryset(self):
        studentGrade = self.kwargs['studentGrade']
        queryset = Student.objects.filter(grade=studentGrade)
        data = {'students': queryset, 'grade': studentGrade}
        return data

# Function Based View
# def StudentView(request, studentGrade):
#     # studentGrade = request.GET.get('studentGrade')
#     student_list = Student.objects.filter(grade=studentGrade)
#     data = {'data': {'students': student_list, 'grade': studentGrade}}
#     return render(request, 'student_list.html', data)


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
