from django.views.generic import ListView
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer


class GradeView(ListView):
    template_name = "students_by_grade.html"

    def get_queryset(self):
        """
        Returns queryset containing all students of a certain grade.
        """
        return Student.objects.filter(grade=self.kwargs['grade'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grade'] = self.kwargs['grade']
        return context


class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Viewset providing "list" and "detail" REST API actions for Students.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
