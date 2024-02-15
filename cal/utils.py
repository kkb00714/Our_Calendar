from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event

# Python의 HTMLCalendar 클래스를 상속받아
# formatday, formatweek 및 formatmonth 메서드를 재정의
# => Calendar 클래스가 HTMLCalendar 의 일부 메서드를 재정의해서 사용

class Calendar(HTMLCalendar):
    # HTMLCalendar 클래스를 상속하여 새로운 'Calendar' 클래스 정의
    def __init__(self, year=None, month=None):
        # 'Calendar' 클래스의 생성자. 
        # 'year' 과 'month' 인자를 받아들임.
        self.year = year
        self.month = month
        super(Calendar, self).__init__()
        
    def formatday(self, day, events):
        # 날짜(day) 를 포맷하는 메서드 
        # 특정 날짜에 해당하는 이벤트를 필터링하여 HTML 형식으로 반환
        events_per_day = events.filter(start_time__day=day)
        d = ''
        # 이벤트를 HTML 형식으로 포맷한 문자열을 저장하기 위한 빈 문자열 생성
        
        for event in events_per_day:
            d += f'<li> {event.title} </li>'
            # 필터링된 이벤트의 제목을 li 태그로 감싸서 문자열 d에 추가
            
        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
            # 날짜가 유효한 경우 span 태그로 감싸서 반환
        return '<td></td>'
            # 날짜가 0인 경우, 빈 칸 반환
            
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
            # 날짜와 그 요일을 나타내는 튜플 리스트
            # 각 날짜와 요일에 대해 반복함
        return f'<tr> {week} </tr>'
        # HTML 형식으로 포맷된 week 반환
    
    def formatmonth(self, withyear=True):
        events = Event.objects.filter(start_time__year = self.year, start_time__month = self.month)
        # 현재 연도와 월에 해당하는 이벤트를 DB에서 가져와 events 변수에 저장
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        # HTML 테이블로 시작하는 달력 생성
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        # 현재 연도, 월에 해당하는 달의 이름을 HTML 텍스트로 추가
        cal += f'{self.formatweekheader()}\n'
        # 테이블의 요일 헤더를 HTML 텍스트로 추가
        
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
            # 현재 연도, 월에 해당하는 날짜로 주별로 그룹화
        return cal
    
    