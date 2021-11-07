from django.shortcuts import get_object_or_404, render, redirect
from django.utils.safestring import mark_safe

from workspaces.models import Workspace
from .models import Schedule
from .forms import ScheduleForm
from .calendar import Calendar
import datetime
import calendar
from django.http import JsonResponse


def schedule_list(request, workspace_pk):
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


def schedule_create(request, workspace_pk):
    workspace = get_object_or_404(Workspace, pk=workspace_pk)
    if request.method == 'POST':
      form = ScheduleForm(request.POST)
      if form.is_valid():
        schedule = form.save(commit=False)
        schedule.author = request.user
        schedule.workspace = workspace
        schedule.save()
        return redirect('schedules:schedule_list', workspace_pk)
    else:
      form = ScheduleForm()
    context = {
        'form': form,
    }
    return render(request, 'schedules/index.html', context)


def schedule_update(request, workspace_pk, schedule_pk):
    schedule = get_object_or_404(Schedule, pk=schedule_pk)
    if request.user == schedule.author:
      if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
          form.save()
          return redirect('schedules:schedule_list', workspace_pk)
      else:
        form = ScheduleForm(instance=schedule)
    else:
      return redirect('schedules:schedule_list', workspace_pk)
    context = {
        'workspace_pk': workspace_pk,
        # 'form': form,
    }
    return JsonResponse(context)


def schedule_delete(request, workspace_pk, schedule_pk):
    schedule = get_object_or_404(Schedule, pk=schedule_pk)
    if request.user.is_authenticated:
        if request.user == schedule.user: 
            schedule.delete()
            return redirect('schedules:schedule_list', workspace_pk)
    return redirect('schedules:schedule_list', workspace_pk)
