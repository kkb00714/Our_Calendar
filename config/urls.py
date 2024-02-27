# 프로젝트 전체의 URL 패턴 정의 

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cal.urls')),
    # path('accounts/',  include('accounts.urls')), 
]

