from django.forms import ModelForm
from django import forms

from .models import Sales, WeeklyData, Twinkle, AnnualTarget


class SalesForm(ModelForm):
    class Meta:
        model = Sales
        fields = '__all__'


class WeeklyDataForm(ModelForm):
    class Meta:
        model = WeeklyData
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(format=('%Y-%m-%d'),
                                          attrs={'class': 'form-control', 'placeholder': 'Select Date',
                                                 'type': 'date'}),
            'end_date': forms.DateInput(format=('%Y-%m-%d'),
                                        attrs={'class': 'form-control', 'placeholder': 'Select Date', 'type': 'date'})
        }


class TwinkleForm(ModelForm):
    class Meta:
        model = Twinkle
        fields = "__all__"


class AnnualTargetForm(ModelForm):
    class Meta:
        model = AnnualTarget
        fields = "__all__"
