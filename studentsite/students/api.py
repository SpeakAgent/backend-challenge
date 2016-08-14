from models import Student
from serializers import StudentSerializer
from django.http import Http404

from rest_framework.view import APIView
from rest_framework.response import Response

class StudentList(APIView):
    students = Student.objects.all(is_active=True)
    serialized_students = StudentSerializer(students, many=True)
    return Response(serialized_students.data)


