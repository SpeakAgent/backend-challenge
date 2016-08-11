from django.shortcuts import render
from rest_framework import viewsets

from .models import Student, StudentSerializer


def students_list(request):
    """Display list of students. Optionally filter by grade."""
    students = Student.objects

    grade = request.GET.get("grade")
    if grade:
        students = students.filter(grade=grade)

    students = students.order_by("last_name")

    page_title = "All Students"
    if grade:
        page_title = "Students in grade {}".format(grade)

    return render(request, "students/students_list.html", dict(
        grade=grade, page_title=page_title, students=students))


class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
