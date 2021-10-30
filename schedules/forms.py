from django import forms
from .models import Schedule


class DateInput(forms.DateInput):
    input_type = 'date'


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
            
    class Meta:
        model = Schedule
        exclude = ('author','workspace',)
        widgets = {
            'start_date' : DateInput(),
            'end_date' : DateInput()
        }