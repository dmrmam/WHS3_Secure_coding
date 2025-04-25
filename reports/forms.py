from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['reason']
        labels = {'reason': '신고 사유'}
        widgets = {
            'reason': forms.Textarea(attrs={'rows': 4, 'placeholder': '신고 사유를 입력하세요.'})
        }