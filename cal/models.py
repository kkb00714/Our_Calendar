from django.db import models
from django.utils import timezone

# 캘린더에 추가할 기능

# 이벤트 (일정)
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField(default=timezone.now, editable=True)
    end_time = models.DateTimeField(default=timezone.now, editable=True)
    

