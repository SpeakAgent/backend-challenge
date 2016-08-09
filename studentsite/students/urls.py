from django.conf.urls import url
from django.conf.urls import include

from .views import StudentView
from .views import StudentViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    # Class Based View url
    url(r'^$', StudentView.as_view(), name='students'),

    # Function Based View url
    # url(r'^$', StudentView, name='students')

    url(r'^api/', include(router.urls)),
]
