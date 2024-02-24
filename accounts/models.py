from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# AbstractBaseUser : 장고에서 제공하는 기본 사용자 모델을 확장할 때 사용되는 Abstract Class
# 이 클래스를 상속하여 커스텀 가능

class User(AbstractBaseUser):
    username = models.CharField(max_length = 16, unique = True)
    # unique 속성 => 해당 필드의 값이 고유해야 함을 의미. 

    email = models.EmailField(max_length = 255, unique = True)
    password = models.CharField(max_length = 32)
    password_confirm = models.CharField(max_length = 32)
    nickname = models.CharField(max_length = 12)
    
    USERNAME_FIELD = 'email'
    # 사용자를 식별하는 필드를 지정하는 변수로, 사용자 인증을 할 때 이메일을 사용하도록 함
    
    # AbstractBaseUser 를 상속하여 커스텀 사용자 모델을 정의할 때,
    # 사용자를 식별하는 필드를 'username' 외에 다른 것으로 지정 가능

    REQUIRED_FIELDS = ['username', 'email','password', 'password_confirm', 'nickname']
    # 사용자를 생성할 때 필수로 입력해야 하는 필드들을 지정하는 변수.
    # 이 필드들은 사용자를 생성할 때 반드시 입력되어야 함.
    