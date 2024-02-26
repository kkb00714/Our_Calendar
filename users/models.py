from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager

class UserManager(DjangoUserManager):
    def _create_user(self, username, email, password, nickname=None, **extra_fields):
        if not email:
            raise ValueError('이메일은 필수 값 입니다.')

        user = self.model(username=username, email=email, nickname=nickname, **extra_fields)
        # 사용자 모델 생성
        user.set_password(password)
        # set_password => 사용자의 비밀번호를 해싱하여 저장함
        user.save()
        # 사용자 저장
        
    def create_user(self, username, email=None, password=None, nickname=None, **extra_fields):
        # 일반 사용자 생성 (기본적으로 staff, superuser 기능은 False 처리)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, nickname, **extra_fields)
            
    def create_superuser(self, username, email=None, password=None, nickname=None, **extra_fields):
        # 관리자 생성 ( 기본적으로 staff, superuser 설정)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password, nickname, **extra_fields)

class User(AbstractUser):
    # 커스텀 사용자 모델 정의 (선택적으로 작성)
    profile_picture = models.ImageField(verbose_name='프로필 사진', upload_to='profiles/', blank=True, null=True)
    phone = models.CharField(verbose_name='전화번호', max_length=11)
    address = models.CharField(verbose_name='주소', max_length=255, blank=True, null=True)
    birthday = models.DateField(verbose_name='생일', blank=True, null=True)
    social_media_accounts = models.CharField(verbose_name='소셜 미디어', max_length=255, blank=True, null=True)
    
    objects = UserManager()
