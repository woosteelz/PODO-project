import calendar
from .models import Schedule


class Calendar(calendar.HTMLCalendar):
	cssclasses = ["월", "화", "수", "목", "금", "토", "일"]

	def __init__(self, year=None, month=None):
		self.firstweekday = 6  # 왜 안바뀌지?!!!! sun = 6, mon = 0
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# '일'을 td 태그로 변환
	def formatday(self, day, schedules):
		schedules_per_day = schedules.filter(start_date__day__lte=day, end_date__day__gte=day)
		d = ''
		for schedule in schedules_per_day:
			schedule_pk = schedule.pk
			workspace_pk = schedule.workspace.pk
			schedule_title = schedule.title
			schedule_content = schedule.content
			schedule_priority = schedule.priority
			schedule_start_date = schedule.start_date.strftime('%Y-%m-%d')
			schedule_end_date = schedule.end_date.strftime('%Y-%m-%d')
			if type(schedule.start_time) != type(None):
				schedule_start_time = schedule.start_time.strftime('%H:%M:%S')
			else:
				schedule_start_time = 0

			if type(schedule.end_time) != type(None):
				schedule_end_time = schedule.end_time.strftime('%H:%M:%S')
			else:
				schedule_end_time = 0

			if schedule_priority == '1':
				new_schedule_title = '🔴 ' + schedule_title
			elif schedule_priority == '2':
				new_schedule_title = '🟡 ' + schedule_title
			else:
				new_schedule_title = '🟢 ' + schedule_title
			
			if len(new_schedule_title) > 7:
				new_schedule_title = new_schedule_title[:7]+'...'

			d += (
				f"<li type='button' data-schedule-id='{schedule_pk}' data-workspace-id='{workspace_pk}' data-schedule-title='{schedule_title}' data-schedule-content = '{schedule_content}'"
				f"data-schedule-priority='{schedule_priority}' data-schedule-start-date='{schedule_start_date}' data-schedule-end-date='{schedule_end_date}'"
				f"data-schedule-start-time='{schedule_start_time}' data-schedule-end-time='{schedule_end_time}'"
				f"data-toggle='modal' data-target='#updateModal'>{new_schedule_title}</li>"
			)
				
		if day != 0:
			if day < 10 :
				return f"<td><span class='schedules_date'>0{day}</span><div><ul class='schedule_list'> {d} </ul></div></td>"
			return f"<td><span class='schedules_date'>{day}</span><div><ul class='schedule_list'> {d} </ul></div></td>"
		return '<td></td>'

	
	# '주'를 tr 태그로 변환
	def formatweek(self, theweek, schedules):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, schedules)
		return f'<tr> {week} </tr>'

	
	# '월'을 테이블 태그로 변환
	# 각 '월'과 '연으로 스케줄 필터
	def formatmonth(self, withyear=True):
		schedules = Schedule.objects.filter(start_date__year=self.year, start_date__month=self.month)

		cal = f'<table class="schedules_calendar">\n'
		#cal += f'<tr><th colspan="7" class="schedules_date">{self.year}년 {self.month}월</th></tr>\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, schedules)}\n'
		return cal