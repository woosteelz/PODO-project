from django import forms
from .models import Schedule

PRIORITY = [
    ('1', 'very important'),
    ('2', 'important'),
    ('3', 'normal'),
]

class ScheduleForm(forms.ModelForm):
    title = forms.CharField(
        label='일정 제목',
        widget=forms.TextInput(
            attrs={
                'class':'my-shedule-title',
                'placeholder': '일정 제목을 입력해주세요.',
                'maxlength': 50,
                }
                ),
            error_messages={
                'required': '일정 제목이 입력되지 않았습니다.'
                }
            )
    
    content = forms.CharField(
        label='일정 내용',
        widget=forms.Textarea(
            attrs={
                'class':'my-schedule_content',
                'placeholder': '내용을 입력해주세요.',
                'rows': 5,
                'cols': 50,
                }
            ),
            error_messages={
                'required':'내용이 입력되지 않았습니다!'
                }
            )

    priority = forms.CharField(
        label='',
        widget=forms.RadioSelect(
            choices=PRIORITY,
            attrs={
                'class': 'schedule-priority',
            }
        ),
    )
            
    class Meta:
        model = Schedule
        widgets = {
            'start_date' : forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'end_date' : forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'start_time' : forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'),
            'end_time' : forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'),
        }
        exclude = ('author','workspace',)


    def __init__(self, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].input_formats = ('%Y-%m-%d',)
        self.fields['end_date'].input_formats = ('%Y-%m-%d',)
        self.fields['start_time'].input_formats = ('%H-%M',)
        self.fields['end_time'].input_formats = ('%H-%M',)