from django.http import HttpResponse
from django.shortcuts import render
from models import Student

def index(request):
    student_list = Student.objects.order_by('last_name')
    return HttpResponse(student_list)
