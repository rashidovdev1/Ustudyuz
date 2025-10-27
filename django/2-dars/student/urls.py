from django.urls import path

from student.views import get_home, get_about, get_service, get_result, get_course, get_kunuz

urlpatterns = [
    path('', get_home, name='home'),
    path('about/', get_about, name='about'),
    path('service/', get_service, name='service'),
    path('result', get_result, name='result'),
    path('course', get_course, name='course'),
    path('kunuz/', get_kunuz, name='kunuz'),
]