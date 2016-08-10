from django.conf.urls import url

from . import views


urlpatterns = [
    url(r"^$", views.students_list, name="students_list")
]
