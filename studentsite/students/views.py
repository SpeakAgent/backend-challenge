from django.http import HttpResponse
from django.template import loader

from models import Student

def index(request):
    student_list = Student.objects.order_by('last_name')
    template = loader.get_template('students/index.html')
    context = {
        'student_list': student_list,
    }
    return HttpResponse(template.render(context, request))
