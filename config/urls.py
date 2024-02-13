# 프로젝트 전체의 URL 패턴 정의 

from django.contrib import admin
from django.urls import path, include
from cal.views import index

app_name = 'cal'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('cal.urls')),
    
]

