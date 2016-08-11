from django.shortcuts import render
from models import Student

def index():
    student_list = Student.objects.order_by('last_name')
    return student_list
