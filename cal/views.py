from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from datetime import datetime
from .models import *
from .utils import Calendar

class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/cal.html' 
    # 템플릿 파일 경로 지정
    # DB에서 달력에 보여줄 이벤트를 가져오는 view
    # 이 view는 cal/calendar.html 파일과 연결

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 기본적인 context 데이터를 가져옴. (ListView의)
        d = self.get_date(self.request.GET.get('day', None))
            # 현재 달력에 보여줄 
            # 년도, 월 정보를 가져와 context 인스턴스에 생성
        
        cal = Calendar(d.year, d.month)
        
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        # mark_safe 함수를 사용하여 HTML코드를 안전하게 처리하고 
        # context를 달력에 전달
        
        return context
    
    def get_date(self, req_day):
        if req_day:
            year, month = (int(x) for x in req_day.split('-'))
            # 입력받은 날짜를 하이픈으로 분리. 
            # 분리된 문자열을 숫자로 변환하여 연도, 월로 변환(정수)하여
            # 연도와 월을 나타내는 튜플 생성
            
            return datetime(year, month, day=1)
            # 사용자가 요청한 날짜를 파싱하여 datetime 객체로 변환
        return datetime.today()
            # 날짜가 없으면 현재 날짜를 가져와서 datetime 객체를 반환
