from django.conf.urls import url

from .views import StudentView

urlpatterns = [
    #Class Based View url
    url(r'^$', StudentView.as_view(), name='students'),

    #Function Based View url
    # url(r'^$', StudentView, name='students')
]
