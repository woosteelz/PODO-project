from django.shortcuts import get_object_or_404, render, redirect
from django.utils.safestring import mark_safe
from workspaces.models import Workspace
from .models import Schedule
from .forms import ScheduleForm
from .calendar import Calendar
import datetime
import calendar
from django.http import JsonResponse


def index(request, workspace_pk):
    today = get_date(request.GET.get('month'))

    prev_month_url = prev_month(today)
    next_month_url = next_month(today)

    calendar = Calendar(today.year, today.month)
    # calendar.setfirstweekday(calendar.SUNDAY)
    html_calendar = calendar.formatmonth(withyear=True)
    form = ScheduleForm()
    context = {
      'calender': mark_safe(html_calendar),
      'prev_month_url': prev_month_url,
      'next_month_url': next_month_url,
      'workspace_pk': workspace_pk,
      'year': today.year,
      'month': today.month,
      'form': form,
    }
    return render(request, 'schedules/index.html', context)


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime.date(year, month, day=1)
    return datetime.datetime.today()


def prev_month(day):
    first = day.replace(day=1)
    prev_month = first - datetime.timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(day):
    days_in_month = calendar.monthrange(day.year, day.month)[1]
    last = day.replace(day=days_in_month)
    next_month = last + datetime.timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def create_schedule(request, workspace_pk):
    workspace = get_object_or_404(Workspace, pk=workspace_pk)
    if request.method == 'POST':
      form = ScheduleForm(request.POST)
      if form.is_valid():
        schedule = form.save(commit=False)
        schedule.author = request.user
        schedule.workspace = workspace
        schedule.save()
    print('저장X')
    return redirect('schedules:index', workspace_pk)
    


def update_schedule(request, workspace_pk, schedule_pk):
    schedule = get_object_or_404(Schedule, pk=schedule_pk)
    if request.user == schedule.author:
        if request.method == 'POST':
            form = ScheduleForm(request.POST, instance=schedule)
            if form.is_valid():
                form.save()
            return redirect('schedules:index', workspace_pk)
        else:
            schedule_title = schedule.title
            schedule_content = schedule.content
            schedule_priority = schedule.priority
            schedule_start_date = schedule.start_date.strftime('%Y-%m-%d')
            schedule_end_date = schedule.end_date.strftime('%Y-%m-%d')
            schedule_start_time = schedule.start_time.strftime('%H:%M:%S')
            schedule_end_time = schedule.end_time.strftime('%H:%M:%S')
            context = {
                'schedule_title': schedule_title,
                'schedule_content': schedule_content,
                'schedule_priority': schedule_priority,
                'schedule_start_date': schedule_start_date,
                'schedule_end_date': schedule_end_date,
                'schedule_start_time': schedule_start_time,
                'schedule_end_time': schedule_end_time,
            }
            return JsonResponse(context)



def delete_schedule(request, workspace_pk, schedule_pk):
    schedule = get_object_or_404(Schedule, pk=schedule_pk)
    if request.user.is_authenticated:
        if request.user == schedule.author: 
            schedule.delete()
            print('삭제완료')
            return redirect('schedules:index', workspace_pk)
    return redirect('schedules:index', workspace_pk)