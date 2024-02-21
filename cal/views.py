from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from datetime import datetime, timedelta
import calendar

from .models import *
from .utils import Calendar

class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/cal_base.html' 
    # 템플릿 파일 경로 지정
    # DB에서 달력에 보여줄 이벤트를 가져오는 view
    # 이 view는 cal/cal_base.html 파일과 연결

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
        
        # 기능1 (이전 달, 다음 달으로 넘어가기)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        
        return context
    
    def get_date(self, req_day):
        try:
            if req_day:
                year, month, day = (int(x) for x in req_day.split('-'))
                # 입력받은 날짜를 하이픈으로 분리. 
                # 분리된 문자열을 숫자로 변환하여 연도, 월로 변환(정수)하여
                # 연도와 월을 나타내는 튜플 생성
                
                return datetime(year, month, day=1)
                # 사용자가 요청한 날짜를 파싱하여 datetime 객체로 변환
        except (ValueError, TypeError):
            # ValueError, TypeError예외가 발생할 경우 처리 (pass)
            # 요청 날짜가 잘못된 형식일 때 발생
            pass
        return datetime.today().date()

def prev_month(d): # 주어진 날짜의 이전 달 계산
    first = d.replace(day=1)
    # 입력받은 날짜 'd' 의 첫 번째 날을 나타내는 새로운 datetime 객체(first) 생성

    prev_month = first - timedelta(days=1)
    # first에서 하루를 빼서 이전 달의 마지막 날을 나타내는 새로운 datetime 객체(prev_month) 생성

    month = 'day=' + str(prev_month.year) + '-' + str(prev_month.month) + '-' + str(prev_month.day)
    # prev_month의 연 월 일을 문자열로 변환하여 반환
    return month

def next_month(d): # 주어진 날짜의 다음 달 계산
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    # 현재 월, 일 수를 계산

    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
        # 현재 월의 마지막 날짜로부터 1일 뒤의 날짜를 게산하여 다음 달의 첫 번째 날을 구함

    month = 'day=' + str(next_month.year) + '-' + str(next_month.month) + '-' + str(next_month.day)
    # 다음 달의 연 월 일을 문자열로 변환하여 반환
    return month
