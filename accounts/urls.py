from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),  # 회원가입 페이지 URL
    path('login/', views.login, name='login'),  # 로그인 페이지 URL
]
