import calendar
from .models import Schedule


class Calendar(calendar.HTMLCalendar):
	cssclasses = ["월", "화", "수", "목", "금", "토", "일"]

	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# '일'을 td 태그로 변환
	def formatday(self, day, schedules):
		schedules_per_day = schedules.filter(start_date__day=day)
		d = ''
		for schedule in schedules_per_day:
			schedule_pk = schedule.pk
			workspace_pk = schedule.workspace.pk
			d += (
				f"<li><button' type='button' class=' btn btn-link' data-bs-toggle='modal' data-bs-target='#exampleModal'>{schedule.title}</button></li>"
				f"<div class='modal fade' id='exampleModal' tabindex='-1' aria-labelledby='exampleModalLabel' aria-hidden='true'>"
				f"<div class='modal-dialog modal-lg modal-dialog-centered'>"
				f"<div class='modal-content'>"
				f"<div class='modal-body'>"
				f"<form id='scheduleForm' class='container' action='/schedules/workspace/{schedule.workspace.pk}/schedule/{schedule.pk}/update' {schedule.title}' method='POST'>"
				f"{{% csrf_token %}}"
				f"{{{{ form.as_p }}}}"
				f"<button class='btn btn-secondary' type='submit' > Submit </button>"
				f"<button class='btn btn-secondary' data-bs-dismiss='modal'>Close</button>"
				f"</form></div></div>/div></div>"
			)
				
		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
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

		cal = f'<table class="calendar">\n'
		#cal += f'<tr><th colspan="7" class="month">{self.year}년 {self.month}월</th></tr>\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, schedules)}\n'
		return cal