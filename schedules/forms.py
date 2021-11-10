from django import forms
from .models import Schedule


PRIORITY = [
    ('1', '🔴'),
    ('2', '🟡'),
    ('3', '🟢'),
]

class ScheduleForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'class':'my-schedule-title',
                'maxlength': 50,
                'rows': 1,
                }
                ),
        error_messages={
            'required': '일정 제목이 입력되지 않았습니다.'
            }
        )
    
    content = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'class':'my-schedule-content',
                'rows': 3,
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
                'class': 'my-schedule-priority',
                }
            )
        )

    start_date = forms.DateField(
        label='',
        widget=forms.DateInput(
            attrs={'type': 'date','class': 'my-schedule-start_date'}, 
            format='%Y-%m-%d'
            )
        )

    end_date = forms.DateField(
        label='',
        widget=forms.DateInput(
            attrs={'type': 'date','class': 'my-schedule-end_date'}, 
            format='%Y-%m-%d'
            )
        )
    start_time = forms.TimeField(
        label='',
        widget=forms.TimeInput(
            attrs={'type': 'time', 'class': 'my-schedule-start_time'},
            format='%p %I:%M'
            ),
        required=False
        )

    end_time = forms.TimeField(
        label='',
        widget=forms.TimeInput(
            attrs={'type': 'time', 'class': 'my-schedule-end_time'},
            format='%p %I:%M'
            ),
        required=False
        )

            
    class Meta:
        model = Schedule
        exclude = ('author','workspace','favorite_users')


    def __init__(self, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].input_formats = ('%Y-%m-%d',)
        self.fields['end_date'].input_formats = ('%Y-%m-%d',)
