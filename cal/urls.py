# cal 앱의 url 패턴을 정의

from django.urls import path
from . import views

app_name = 'cal'

urlpatterns = [
    path('', views.CalendarView.as_view(), name='calendar'),
]
