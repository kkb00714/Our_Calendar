# cal 앱의 url 패턴을 정의

from django.urls import path
from . import views

app_name = 'cal'

urlpatterns = [
    path('calendar/', views.CalendarView.as_view(template_name = 'cal/cal.html'), name='calendar'),
    path('eventform/', views.add_event, name='eventform'),
]
