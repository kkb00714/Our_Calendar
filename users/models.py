from django.db import models
from django.utils import timezone

# 사용자 모델
class User(models.Model):
    username = models.CharField(verbose_name='사용자 아이디', max_length=12, unique=True, blank=False, null=False)
    email = models.EmailField(verbose_name='이메일', unique=True, blank=False, null=False)
    password = models.CharField(verbose_name='비밀번호', max_length=28, blank=False, null=False)  # 비밀번호는 해싱하여 저장하는 것이 안전합니다.
    nickname = models.CharField(verbose_name='닉네임', max_length=10, unique=True, blank=False, null=False)
    phone = models.CharField(verbose_name='전화번호', max_length=11, blank=True, null=True)
    address = models.CharField(verbose_name='주소', max_length=255, blank=True, null=True)
    birthday = models.DateField(verbose_name='생년월일', blank=True, null=True)
    social_media_accounts = models.JSONField(verbose_name='소셜 미디어 계정', default=dict, blank=True, null=True)
    profile_picture = models.ImageField(verbose_name='프로필 사진', upload_to='profiles/', blank=True, null=True)
    
# 따로 분리한 이유
# 데이터 관리와 관련된 코드와 비즈니스 로직 분리를 위해.
# => 나중에 코드를 재사용하거나 다른 앱에서도 쉽게 이용 가능!